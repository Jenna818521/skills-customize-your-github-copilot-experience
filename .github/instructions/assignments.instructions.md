---
description: "Instructions to use whenever creating or editing assignment markdown files to ensure consistency and clarity for students."
applyTo: "assignments/**/*.md"
---

# Assignment Markdown Structure Guidelines

All assignment markdown files must be named `README.md` and follow [`templates/assignment-template.md`](../../templates/assignment-template.md). Preserve the template's section order and headings:

- `# 📘 Assignment: [Assignment Title]`
- `## 🎯 Objective`
- `## 📝 Tasks`
- For each task: `### 🛠️ [Task Title]`, `#### Description`, and `#### Requirements`
- Keep the line `Completed program should:` before the requirement bullets.

## 1. Template Usage

- Replace bracketed placeholders with assignment-specific content; do not leave template placeholders in a completed assignment.
- Include one or more task sections as appropriate. Do not remove required headings or add sections unless explicitly requested.

## 2. Section Guidance

- **Title**: Use a short, descriptive assignment name.
- **Objective**: Write 1-2 sentences describing the learning goals and what students will accomplish.
- **Tasks**: For each task:
   - Use a specific, action-oriented title.
   - Clearly explain what the student must do in **Description**.
   - List expected behavior or deliverables as specific, measurable bullets under **Requirements**.
   - Include input/output examples in fenced code blocks when they clarify the expected result.

## 3. Educational Standards

- Keep assignments learning-focused, appropriate to the stated concepts, and clear for students.
- Use encouraging, student-friendly language.
- Ensure requirements are consistent with the assignment's starter code and included data files.

Do not add unrelated sections or requirements.
