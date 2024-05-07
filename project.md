# Optimization Project: Refine the Algorithm for the Annual SEP Assignment

## Project Overview

If you have participated in the Software Entwicklungs Praktikum (SEP), you are likely familiar with the student assignment system currently in use. The process begins with supervisors specifying projects and their capacity limits. Students submit their preferences for projects and potential team partners, along with detailed skill profiles. Supervisors then evaluate these entries, endorsing or vetoing students based on their suitability. They can also issue explicit rejections for students with whom there have been past issues. However, the decision-making process heavily favors student preferences, often overlooking other important factors.

## Project Objective

Your task is to design a more sophisticated algorithm that refines this process, incorporating a fully functional system demonstrable to the SEP organizer. This system should improve on multiple fronts:

### Data Collection

Refine the data collection mechanism to capture comprehensive, algorithm-specific information from students and supervisors. Consider including:

- Detailed preferences for projects and team partners.
- Comprehensive skill sets and proficiencies.
- Supervisor requirements and preferences concerning student capabilities and project needs.
- Specifications on minimum and maximum student counts per project.
- Thresholds for potential project cancellation.

Evaluate the essential data points to ensure robust assignment outcomes without imposing undue data entry burdens. Utilize user-friendly data collection tools like Streamlit to facilitate input without requiring extensive web development skills.

### Mathematical Model

Construct a mathematical model to precisely outline your optimization objectives and constraints:

- **Objectives:**
    - Maximize the student placement rate within projects.
    - Prioritize assignments based on nuanced student preferences, possibly by allowing students to score rather than rank projects.
    - Facilitate team formations based on preferred partnerships.
    - Integrate supervisor feedback to align student assignments with project skill demands.
    - Target ideal project team sizes to prevent overfilling or underfilling.
- **Constraints:**
    - Enforce specific student capacity ranges for each project, with provisions for cancelling projects that do not meet minimum interest levels.
    - Implement skill-based placements, such as ensuring a balance of front-end and back-end developers or meeting minimum skill prerequisites for projects.

### Implementation

Develop and fine-tune an algorithm that efficiently solves this enhanced model, leveraging the latest in optimization technologies and libraries.

### Output and Benchmarking

- Produce outputs in a machine-readable format that can be easily processed by the SEP organizer.
- Establish benchmarks to gauge the effectiveness of your algorithm in creating optimal group formations based on the identified objectives and constraints.
- Ensure the algorithm's scalability to accommodate scenarios involving up to 1000 students and 100 projects.

### Development Strategy

Initiate the project by developing a foundational model that addresses the core objectives and constraints—primarily, maximizing the assignment of students to their preferred projects while adhering to the group size limitations. Incrementally incorporate more sophisticated objectives and constraints, such as skill matching and supervisor preferences. This phased approach will help manage the complexity of the system, allowing for iterative enhancements and adjustments based on testing and feedback.

This project offers a significant opportunity to apply your optimization skills to a tangible challenge, with the potential to substantially improve the SEP assignment process. We wish you the best in your endeavors to innovate and refine this system.