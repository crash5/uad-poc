#!/usr/bin/env bash
set -e

readonly RELEASE_VERSION=${1:-"19700101010101"}
export RELEASE_VERSION

readonly RELEASE_DOWNLOAD_URL=${2:-"https://"}
export RELEASE_DOWNLOAD_URL

readonly OUTPUT_PATH=${3:-"output/"}


tools/mo templates/version.txt.mustache > "${OUTPUT_PATH}"/version.txt
tools/mo templates/version_with_url.txt.mustache > "${OUTPUT_PATH}"/version_with_url.txt
tools/mo templates/version.json.mustache > "${OUTPUT_PATH}"/version.json
tools/mo templates/index.html.mustache > "${OUTPUT_PATH}"/index.html
