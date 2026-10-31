-----

<div align="center">

[![Poetry](https://img.shields.io/badge/packaging-poetry-cyan.svg)](https://python-poetry.org/)
[![GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

</div>

<hr>

# TOBB ETU CS Community Website

A Streamlit website for the TOBB ETÜ Computer Science Community, with team information, an event calendar, project plans, youth programs, a weekly menu, and a feedback form.

This repository is a fork of [TOBB-ETU-CS-Community/Community_Website](https://github.com/TOBB-ETU-CS-Community/Community_Website).

[Community-hosted app](https://tobbetu-bilgisayar-toplulugu.streamlit.app/)

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before setting up the project, ensure that you have the following prerequisites installed on your machine:

- Python (version 3.10.10):
  (https://www.python.org/downloads/)
- Poetry (version 1.4.0):
  (https://python-poetry.org/docs/#installation)

## Installation

1. Clone the project repository:

```
git clone https://github.com/ataturhan21/Community_Website.git
```

2. Navigate to the project directory:

```
cd Community_Website
```

3. Install project dependencies using Poetry:

```
poetry install
```

This command will create a virtual environment and install all the necessary dependencies specified in the `pyproject.toml` file.

## Usage

Run from the repository root so the relative paths to images, spreadsheets, and styles resolve correctly:

```bash
poetry run streamlit run "community_website/👋Hoşgeldiniz.py"
```

On Windows, `start.bat` runs the same entry point from the repository directory.

## Content and project guide

| Path | Contents |
| --- | --- |
| [Welcome page](community_website/%F0%9F%91%8BHo%C5%9Fgeldiniz.py) | Application entry point |
| [Pages](community_website/pages/) | Team, events, plans, programs, menu, and feedback |
| [Spreadsheets](static/xlsx/) | Team, event, project-plan, and program data |
| [Static assets](static/) | Community imagery, program images, and weekly menu |
| [Utilities](community_website/modules/utils.py) | Excel loading, page configuration, and shared styling |

The spreadsheet loader expects a worksheet named `Sheet1`. Keep the column names and date formats expected by each page when editing the workbooks. Published event and program dates are stored content, so review them before reusing this website for a current community.

The original environment uses Python 3.10 and Poetry 1.4.0. The repository includes `poetry.lock`; this update does not upgrade dependencies.

## Contributing

If you would like to contribute to this project, follow the guidelines below:

1. Fork the repository and clone it locally.

2. Create a new branch for your feature or bug fix:
   ```
   git checkout -b feature/your-feature
   ```

3. Make your changes and commit them with descriptive commit messages.

4. Push your changes to your forked repository:
   ```
   git push origin feature/your-feature
   ```

5. Open a pull request in the original repository, describing your changes in detail.


## License

GPL v3

---
