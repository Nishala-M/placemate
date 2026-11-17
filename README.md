# PlaceMate – MCP-Based Job Application Manager

PlaceMate is a Python-based job application management system built using the **Model Context Protocol (MCP)** and SQLite.

It allows an AI assistant to search for jobs, manage job applications, track application statuses, and retrieve job information through MCP tools and resources.

## Features

- Search jobs by keyword and location.
- Add job applications for students.
- View submitted applications.
- Update application statuses.
- Retrieve job details using an MCP resource.
- Generate interview preparation guidance using an MCP prompt.

## Technologies Used

- Python
- SQLite
- Model Context Protocol (MCP)
- UV – Python package and project manager
- VS Code
- GitHub Copilot

## MCP Tools

| Tool | Description |
|---|---|
| `search_jobs` | Search jobs by keyword and location |
| `add_application` | Add a job application |
| `list_applications` | View applications for a student |
| `update_status` | Update an application status |

## MCP Components

- **Tools:** Perform job-search and application-management operations.
- **Resource:** `jobs://{job_id}` provides job information.
- **Prompt:** `interview_prep` provides reusable interview preparation instructions.

## Project Structure

```text
placemate/
├── database.py
├── models.py
├── server.py
├── pyproject.toml
├── uv.lock
├── README.md
└── .gitignore
```

## Setup and Run

### 1. Clone the repository

```bash
git clone https://github.com/Nishala-M/placemate.git
cd placemate
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Run the MCP server

```bash
uv run python server.py
```

The project uses a local SQLite database. Ensure the database is initialized or seeded according to the setup in `database.py`.

## Testing

The MCP server was tested using MCP Inspector and VS Code with GitHub Copilot.

The four MCP tools were tested for job searching, adding applications, listing applications, and updating application statuses.

## Future Enhancements

- Add user authentication.
- Integrate live job APIs.
- Build a web-based dashboard.
- Add application reminders and notifications.

## Author

**Nishala M**

GitHub: [Nishala-M](https://github.com/Nishala-M)