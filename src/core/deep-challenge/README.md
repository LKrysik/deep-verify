Challenge user (if with deep explore)


---
name: 'deep challenge'
description: 'Challenge user'

# File References
deep-explore: if path provided then read and use it and save location of file, if not execute deep explore


outputFile: '{deep_artifacts}/prd.md'
purposeFile: '../data/prd-purpose.md'

# Task References
deep-explore: '{project-root}/src/core/deep-explore/workflows/md'
---