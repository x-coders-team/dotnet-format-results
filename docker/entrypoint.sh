#!/bin/sh -l

echo "JSON Input $1"
echo "Runner work directory $2"

if pip install githubkit; then
    echo "[OK] pip install githubkit"
else 
    echo "[KO] pip install githubkit"
fi

echo  "GITHUB_SHA: ${GITHUB_SHA} \n"
echo  "GITHUB_REPOSITORY_OWNER: ${GITHUB_REPOSITORY_OWNER} \n"
echo  "GITHUB_REPOSITORY: ${GITHUB_REPOSITORY} \n"
echo  "GITHUB_HEAD_REF: ${GITHUB_HEAD_REF} \n"
echo  "GITHUB_ACTION_REF: ${GITHUB_ACTION_REF} \n"
echo  "GITHUB_TOKEN: ${GITHUB_TOKEN} \n"
echo  "GITHUB_REF: ${GITHUB_REF} \n"
echo  "GITHUB_REF_NAME: ${GITHUB_REF_NAME} \n"
echo  "GITHUB_ACTION_REPOSITORY: ${GITHUB_ACTION_REPOSITORY} \n"
echo  "GITHUB_ACTION_REF: ${GITHUB_ACTION_REF} \n"
echo  "GITHUB_ACTION: ${GITHUB_ACTION} \n"
echo  "GITHUB_WORKFLOW_SHA: ${GITHUB_WORKFLOW_SHA} \n"
echo  "GITHUB_REF_TYPE: ${GITHUB_REF_TYPE} \n"

gitHubConfig="{\"SHA\": \"${GITHUB_SHA}\", \"REPOSITORY_OWNER\": \"${GITHUB_REPOSITORY_OWNER}\", \"REPOSITORY\": \"${GITHUB_REPOSITORY}\"}"

debug_output=$(python /action/src/main.py "$1" "$2" "${gitHubConfig}" "1")
echo "Run With Debug:"
echo "$debug_output"

if html_output=$(python /action/src/main.py "$1" "$2" "${gitHubConfig}" "0"); then
    echo "Prepare output"
    echo "html-output=$html_output" >> $GITHUB_OUTPUT
else
    echo "Unable return HTML output"
    exit 1
fi
