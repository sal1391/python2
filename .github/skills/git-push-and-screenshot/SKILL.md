---
name: git-push-and-screenshot
user-invocable: true
description: "Use this skill to capture the current open file with the screenshot tool, save it into the repo, and optionally stage/commit/push changes."
---

# Git Push and Screenshot Skill

This skill helps you capture a screenshot of the currently open file and save it into the repository, then optionally stage, commit, and push the file.

Use cases:
- Capture the current editor file as a screenshot and save it to the repo
- Create a screenshot file next to the source file
- Stage and commit the screenshot file
- Push the commit to the remote branch

## How to use

Ask for one of the following:
- "Capture a screenshot of this file and upload it to the repo"
- "Take a screenshot of the current open file and commit it"
- "Save the current file screenshot and push it"
- "Stage, commit, and push the screenshot file"

## Behavior

When invoked, the skill should:
1. Identify the currently open file or workspace file to capture
2. Use the `screenshot_page` tool to capture the visible file contents from the browser page
3. Save the screenshot image into the repository folder next to the source file
4. Stage the new screenshot file
5. Commit with a descriptive message such as "Add screenshot for <filename>"
6. Push the new commit to the remote

## Notes

- The screenshot should be saved with a clear filename like `<basename>_screenshot.png`
- If the file is not open in the browser page, load it first before capturing
- This skill is focused on the screenshot workflow and its repository commit/push integration
