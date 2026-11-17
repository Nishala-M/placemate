
from typing import Literal

from mcp.server import MCPServer
from mcp.server.mcpserver.exceptions import (
    ToolError,
    ResourceNotFoundError
)

from database import get_db

from models import (
    search_jobs_db,
    add_application_db,
    list_applications_db,
    update_application_db
)


# Create MCP server
mcp = MCPServer(
    "placemate-jobs",
    instructions=(
        "PlaceMate is a campus placement assistant. "
        "It helps students search jobs and track applications."
    )
)


# TOOL 1: Search jobs
@mcp.tool()
def search_jobs(
    keyword: str = "",
    location: str = ""
) -> list[dict]:
    """Search available jobs using keyword and location."""

    return search_jobs_db(keyword, location)


# TOOL 2: Add application
@mcp.tool()
def add_application(
    student_name: str,
    job_id: int
) -> dict:
    """Save a student's application for a job."""

    if not student_name.strip():
        raise ToolError("Student name cannot be empty.")

    application = add_application_db(student_name, job_id)

    if application is None:
        raise ToolError(
            f"Job ID {job_id} does not exist. "
            "Search for available jobs first."
        )

    return application


# TOOL 3: List applications
@mcp.tool()
def list_applications(student_name: str) -> list[dict]:
    """Show all applications belonging to a student."""

    return list_applications_db(student_name)


# TOOL 4: Update application status
@mcp.tool()
def update_status(
    application_id: int,
    status: Literal[
        "applied",
        "shortlisted",
        "interview",
        "offer",
        "rejected"
    ]
) -> dict:
    """Update the status of a student's application."""

    result = update_application_db(application_id, status)

    if result is None:
        raise ToolError(
            f"Application ID {application_id} does not exist."
        )

    return result


# RESOURCE: Read job details
@mcp.resource("jobs://{job_id}")
def job_details(job_id: int) -> str:
    """Read complete details of a particular job."""

    with get_db() as conn:
        job = conn.execute(
            "SELECT * FROM jobs WHERE id = ?",
            (job_id,)
        ).fetchone()

    if job is None:
        raise ResourceNotFoundError(
            f"No job found with ID {job_id}."
        )

    return (
        f"Job Title: {job['title']}\n"
        f"Company: {job['company']}\n"
        f"Location: {job['location']}\n"
        f"Required Skills: {job['skills']}"
    )


# PROMPT: Interview preparation
@mcp.prompt()
def interview_prep(job_title: str, company: str) -> str:
    """Generate an interview preparation instruction."""

    return (
        f"I have an interview for {job_title} at {company}. "
        "Act as an experienced interviewer. Ask me five technical "
        "questions, one at a time. After each answer, provide feedback "
        "and explain how I can improve."
    )


# Start MCP server
if __name__ == "__main__":
    mcp.run()
