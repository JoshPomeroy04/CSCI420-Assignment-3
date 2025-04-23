import os
import nltk
import json
from sacrebleu.metrics import BLEU
from codebleu import calc_codebleu
import csv

nltk.download('punkt_tab')

FOLDER_PATH = "CSCI_420/CSCI420-Assignment-3"
BLEU_KEYS = ["BugClassificationC++.json", "CodeSummarizationJava.json", "FunctionSummarizationPython.json", 
             "NullDereferenceDetectionJava.json", "PromptfromCodeCommentsPython.json", 
             "SummaryDecompositionC++.json", "SQLSchemaDesignSQL.json", "DataClasstoAPIConversionKotlin.json"]
PYTHON_KEYS = ["BugFixingPython-Off-by-One.json", "ConstructorCompletionPython.json", 
               "CSVParserVariantsPython.json", "FixingFactorialBugPython.json",
               "GeneratingEmailValidatorsPython+Regex.json", "GeneratingFlaskAPIsPython.json",
               "PurposeInferenceCompletionPython.json", "RecursiveFunctionCompletionPython.json"]
JAVA_KEYS = ["BinarySearchCompletionJava.json"]
CPP_KEYS = ["Self-ConsistencyBugFixingC++.json", "LinkedListNodeDeletionC.json"]
JS_KEYS = ["PromptChainingBugIdentificationFixJavaScript.json"]

bleu = BLEU()
gemini_responses = {}
gemini_scores = {}
gpt_responses = {}
gpt_scores = {}
gpt_gemini_R1 = {}
gpt_gemini_R1_scores = {}
gpt_gemini_R2 = {}
gpt_gemini_R2_scores = {}

def read_json_files(folder_path):
    """
    Reads a folder containing JSON files

    Args:
        folder_path (str): The path to the folder containing JSON files

    Returns:
        dict: The data from the JSON files, as a Python dictionary.
    """
    data = {}
    for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                with open(file_path, 'r') as file:
                    data[filename] = json.load(file)

    return data

def calc_codebleu_scores(model, keys, language, dict):
    """
    Calculates codebleu scores for a given list of keys for a specified language

    Args:
        model (dict): Dictionary containing all results to calculate
        keys (list): List of keys to calculate scores for
        language (str): Language that the values of the keys are in
        dict (dict): Dictionary to store results in

    Returns:
        None
    """
    for key in keys:
        reference = model[key]["R1"]
        hypothesis = model[key]["R2"]
        codebleuscore = calc_codebleu([reference], [hypothesis], lang=language, weights=(0.25, 0.25, 0.25, 0.25), tokenizer=None)
        dict[key] = round(codebleuscore["codebleu"] * 100, 2)

def calc_all(model, dict):
    """
    Calculates all BLEU scores for a models outputs

    Args:
        model (dict): Dictionary containing all results to calculate
        dict (dict): Dictionary to store results in

    Returns:
        None
    """
    for key in BLEU_KEYS:
        reference = model[key]["R1"]
        hypothesis = model[key]["R2"]
        bleuscore = bleu.sentence_score(hypothesis, [reference]).score
        dict[key] = round(bleuscore, 2)
        

    calc_codebleu_scores(model, PYTHON_KEYS, "python", dict)
    calc_codebleu_scores(model, JAVA_KEYS, "java", dict)
    calc_codebleu_scores(model, CPP_KEYS, "cpp", dict)
    calc_codebleu_scores(model, JS_KEYS, "javascript", dict)

def save_to_csv(results, file):
    """
    Saves results to a csv file

    Args:
        results (dict): Dictionary containing all results
        file (str): File name to save results in

    Returns:
        None
    """
    with open(f"{FOLDER_PATH}/results/{file}", mode='w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Task", "Score"])
        for key in results.keys():
             csv_writer.writerow([key, results[key]])

def calc_codebleu_scores_intermodel(model1, model2, response, keys, language, dict):
    """
    Calculates codebleu scores for a given list of keys for a specified language

    Args:
        model1 (dict): Dictionary containing all results to calculate from first model's responses
        model2 (dict): Dictionary containing all results to calculate from second model's responses
        response (str): Either R1 or R2 to indicate which responses to compare
        keys (list): List of keys to calculate scores for
        language (str): Language that the values of the keys are in
        dict (dict): Dictionary to store results in

    Returns:
        None
    """
    for key in keys:
        reference = model1[key][response]
        hypothesis = model2[key][response]
        codebleuscore = calc_codebleu([reference], [hypothesis], lang=language, weights=(0.25, 0.25, 0.25, 0.25), tokenizer=None)
        dict[key] = round(codebleuscore["codebleu"] * 100, 2)

def calc_all_intermodel(model1, model2, response, dict):
    """
    Calculates all BLEU scores for a models outputs

    Args:
        model1 (dict): Dictionary containing all results to calculate from first model's responses
        model2 (dict): Dictionary containing all results to calculate from second model's responses
        response (str): Either R1 or R2 to indicate which responses to compare
        dict (dict): Dictionary to store results in

    Returns:
        None
    """
    for key in BLEU_KEYS:
        reference = model1[key][response]
        hypothesis = model2[key][response]
        bleuscore = bleu.sentence_score(hypothesis, [reference]).score
        dict[key] = round(bleuscore, 2)
        

    calc_codebleu_scores_intermodel(model1, model2, response, PYTHON_KEYS, "python", dict)
    calc_codebleu_scores_intermodel(model1, model2, response, JAVA_KEYS, "java", dict)
    calc_codebleu_scores_intermodel(model1, model2, response, CPP_KEYS, "cpp", dict)
    calc_codebleu_scores_intermodel(model1, model2, response, JS_KEYS, "javascript", dict)

gemini_responses = read_json_files(f"{FOLDER_PATH}/data/Gemini Responses/")
gpt_responses = read_json_files(f"{FOLDER_PATH}/data/GPT Responses/")


calc_all(gemini_responses, gemini_scores)
calc_all(gpt_responses, gpt_scores)
calc_all_intermodel(gemini_responses, gpt_responses, "R1", gpt_gemini_R1_scores)
calc_all_intermodel(gemini_responses, gpt_responses, "R2", gpt_gemini_R2_scores)

save_to_csv(gemini_scores, "gemini.csv")
save_to_csv(gpt_scores, "gpt.csv")
save_to_csv(gpt_gemini_R1_scores, "gpt-gemini-R1.csv")
save_to_csv(gpt_gemini_R2_scores, "gpt-gemini-R2.csv")

