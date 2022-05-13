# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: sample_multi_category_classify.py

DESCRIPTION:
    This sample demonstrates how to classify documents into multiple custom categories. For example,
    movie plot summaries can be categorized into multiple movie genres like "Action" and "Thriller",
    or "Comedy" and "Drama", etc. Classifying documents is available as an action type through
    the begin_analyze_actions API.

    For information on regional support of custom features and how to train a model to
    classify your documents, see https://aka.ms/azsdk/textanalytics/customfunctionalities

USAGE:
    python sample_multi_category_classify.py

    Set the environment variables with your own values before running the sample:
    1) AZURE_LANGUAGE_ENDPOINT - the endpoint to your Language resource.
    2) AZURE_LANGUAGE_KEY - your Language subscription key
    3) MULTI_CATEGORY_CLASSIFY_PROJECT_NAME - your Language Studio project name
    4) MULTI_CATEGORY_CLASSIFY_DEPLOYMENT_NAME - your Language Studio deployment name
"""


import os


def sample_classify_document_multi_categories():
    from azure.core.credentials import AzureKeyCredential
    from azure.ai.textanalytics import (
        TextAnalyticsClient,
        MultiCategoryClassifyAction
    )

    endpoint = os.environ["AZURE_LANGUAGE_ENDPOINT"]
    key = os.environ["AZURE_LANGUAGE_KEY"]
    project_name = os.environ["MULTI_CATEGORY_CLASSIFY_PROJECT_NAME"]
    deployment_name = os.environ["MULTI_CATEGORY_CLASSIFY_DEPLOYMENT_NAME"]
    path_to_sample_document = os.path.abspath(
        os.path.join(
            os.path.abspath(__file__),
            "..",
            "./text_samples/custom_classify_sample.txt",
        )
    )

    text_analytics_client = TextAnalyticsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key),
    )

    with open(path_to_sample_document) as fd:
        document = [fd.read()]

    poller = text_analytics_client.begin_analyze_actions(
        document,
        actions=[
            MultiCategoryClassifyAction(
                project_name=project_name,
                deployment_name=deployment_name
            ),
        ],
    )

    document_results = poller.result()
    for doc, classification_results in zip(document, document_results):
        for classification_result in classification_results:
            if not classification_result.is_error:
                classifications = classification_result.classifications
                print(f"\nThe movie plot '{doc}' was classified as the following genres:\n")
                for classification in classifications:
                    print("'{}' with confidence score {}.".format(
                        classification.category, classification.confidence_score
                    ))
            else:
                print("Movie plot '{}' has an error with code '{}' and message '{}'".format(
                    doc, classification_result.code, classification_result.message
                ))


if __name__ == "__main__":
    sample_classify_document_multi_categories()