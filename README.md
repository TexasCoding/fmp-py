<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" alt="project-logo">
</p>
<p align="center">
    <h1 align="center">FMP-PY</h1>
</p>
<p align="center">
    <em>Financial Modeling Prep API Data Python SDK</em>
</p>
<p align="center">
  <img alt="GitHub Actions Workflow Status" src="https://img.shields.io/github/actions/workflow/status/TexasCoding/py-alpaca-api/.github%2Fworkflows%2Ftest-package.yaml">
	<img src="https://img.shields.io/github/license/TexasCoding/fmp-py?style=flat-square&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/TexasCoding/fmp-py?style=flat-square&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/TexasCoding/fmp-py?style=flat-square&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/TexasCoding/fmp-py?style=flat-square&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/precommit-FAB040.svg?style=flat-square&logo=pre-commit&logoColor=black" alt="precommit">
	<img src="https://img.shields.io/badge/Poetry-60A5FA.svg?style=flat-square&logo=Poetry&logoColor=white" alt="Poetry">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=flat-square&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions">
	<img src="https://img.shields.io/badge/pandas-150458.svg?style=flat-square&logo=pandas&logoColor=white" alt="pandas">
</p>

<br><!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary><br>

- [ Overview](#-overview)
- [ Features](#-features)
- [ Repository Structure](#-repository-structure)
- [ Modules](#-modules)
- [ Getting Started](#-getting-started)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Tests](#-tests)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)
</details>
<hr>

##  Overview

### This project is under development, please check back later for updates. 

Fmp-py is an open-source Python library designed to simplify access to comprehensive financial data and company information. It facilitates the retrieval and analysis of historical and intraday financial data, financial statements, and key company metrics by interacting seamlessly with the Financial Modeling Prep API. By extending core functionalities and implementing various financial models, fmp-py ensures accurate data processing and interpretation, making it an invaluable tool for developers and analysts aiming for in-depth financial analysis and decision-making support in their applications.

---

##  Features

|    |   Feature         | Description                                                                                           |
|----|-------------------|-------------------------------------------------------------------------------------------------------|
| ⚙️  | **Architecture**  | The project uses a modular architecture, with core components for API interactions, data retrieval, and analysis. Base classes enable easy extension and integration of additional functionalities. |
| 🔩 | **Code Quality**  | The codebase adheres to strict linting and formatting standards, ensuring high readability and maintainability. Tools like `ruff` and `pre-commit` are used to enforce code quality.    |
| 📄 | **Documentation** | The project includes detailed module-level docstrings and function-level comments. The `pyproject.toml` file outlines dependencies and configurations for clear reference.                |
| 🔌 | **Integrations**  | Integrates with Financial Modeling Prep API for data retrieval. Uses GitHub Actions for CI/CD. Relies on libraries such as `requests`, `pandas`, and `python-dotenv`.                      |
| 🧩 | **Modularity**    | Highly modular, with well-defined classes and methods in separate files. Easy to extend with new functionalities by leveraging base classes.                                       |
| 🧪 | **Testing**       | Automated testing is set up via GitHub Actions. Uses `requests-mock` for unit tests to simulate API interactions, ensuring reliable and repeatable tests.                               |
| ⚡️  | **Performance**   | Designed for efficiency with optimized API calls and data processing techniques. Uses `pandas` for efficient data manipulation and analysis.                                           |
| 🛡️ | **Security**      | Utilizes `python-dotenv` to manage API keys securely. HTTP sessions are handled securely in the `fmp_base.py` module to protect data in transit.                                      |
| 📦 | **Dependencies**  | Key dependencies include `requests`, `pandas`, `python-dotenv`, and testing tools like `requests-mock`. Development tools include `ruff`, `pre-commit`, and `poetry`.                |
| 🚀 | **Scalability**   | The modular architecture and efficient data handling enable easy scaling. Can handle increased data volume and API requests with minimal modifications.                                      |

---

##  Repository Structure

```sh
└── fmp-py/
    ├── .github
    │   └── workflows
    │       └── test-package.yaml
    ├── README.md
    ├── poetry.lock
    ├── pyproject.toml
    ├── pytest.ini
    ├── src
    │   └── fmp_py
    │       ├── __init__.py
    │       ├── fmp_base.py
    │       ├── fmp_company_information.py
    │       ├── fmp_historical_data.py
    │       ├── fmp_statement_analysis.py
    │       └── models
    │           ├── company_information.py
    │           └── statement_analysis.py
    └── tests
        ├── __init__.py
        ├── test_fmp_company_information.py
        ├── test_fmp_historical_data.py
        └── test_fmp_statement_analysis.py
```

---

##  Modules

<details closed><summary>.</summary>

| File                                                                               | Summary                                                                                                                                                                                                                                                                                                                            |
| ---                                                                                | ---                                                                                                                                                                                                                                                                                                                                |
| [pyproject.toml](https://github.com/TexasCoding/fmp-py/blob/master/pyproject.toml) | Defines the projects metadata, dependencies, and configurations for both development and testing. Specifies dependencies like requests, pandas, and python-dotenv, along with development tools such as ruff and pre-commit. Configures linting, formatting, and build system settings to ensure code quality and maintainability. |

</details>

<details closed><summary>src.fmp_py</summary>

| File                                                                                                                  | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---                                                                                                                   | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [fmp_historical_data.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_historical_data.py)         | Facilitate access to historical and intraday financial data, supporting various time intervals and date ranges. Enhance data with Volume Weighted Average Price (VWAP) calculations and standardized formatting. Integrate seamlessly with the repositorys architecture by extending FmpBase for consistent API interactions.                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [fmp_statement_analysis.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_statement_analysis.py)   | The `fmp_statement_analysis.py` file defines the `FmpStatementAnalysis` class, which focuses on retrieving and processing financial statement analysis data, such as financial scores, ratios, and key metrics. This class acts as a bridge between raw financial data and its structured, meaningful interpretation, making it a critical component for applications or services requiring in-depth financial analysis. Positioned within the `fmp_py` module, this class leverages base functionalities from `fmp_base.py` and integrates several financial models, ensuring seamless data retrieval and manipulation aligned with the overall financial management and processing objectives of the repository.                                       |
| [fmp_company_information.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_company_information.py) | The `fmp_company_information.py` file is a part of the `fmp-py` repository, specifically within the `src/fmp_py` directory. This module is designed to handle company information within the context of the repositorys architecture. The primary purpose of this module is to define the `FmpCompanyInformation` class, which extends the base functionality provided by the `FmpBase` class. This class facilitates the retrieval and processing of various company-related data, including core information, market capitalization, and company profiles. By integrating these functionalities, the module supports the broader objectives of the repository, which include comprehensive data analysis and management for financial and market data. |
| [fmp_base.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_base.py)                               | Initialize the base functionality for interacting with the Financial Modeling Prep API, managing API keys, handling HTTP sessions, and executing GET requests. Essential for the repositorys architecture, enabling smooth communication with the API and serving as the foundation for other modules to retrieve financial data.                                                                                                                                                                                                                                                                                                                                                                                                                        |

</details>

<details closed><summary>src.fmp_py.models</summary>

| File                                                                                                                 | Summary                                                                                                                                                                                                                                                                 |
| ---                                                                                                                  | ---                                                                                                                                                                                                                                                                     |
| [statement_analysis.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/models/statement_analysis.py)   | Define financial metrics and key ratios related to company performance to facilitate comprehensive financial statement analysis within the repositorys architecture for enhanced decision-making.                                                                       |
| [company_information.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/models/company_information.py) | Model definitions for core company information, market capitalization, executive compensation, and company profiles essential for encapsulating and handling structured company data, supporting various functions and modules in the repositorys overall architecture. |

</details>

<details closed><summary>.github.workflows</summary>

| File                                                                                                       | Summary                                                                                                                                                                                                                                                                                                                              |
| ---                                                                                                        | ---                                                                                                                                                                                                                                                                                                                                  |
| [test-package.yaml](https://github.com/TexasCoding/fmp-py/blob/master/.github/workflows/test-package.yaml) | Automates the testing process for the repository by defining a GitHub Actions workflow. Ensures continuous integration with tasks such as running tests and verifying code quality whenever changes are pushed or pull requests are made. Facilitates rapid feedback and maintains code reliability within the development pipeline. |

</details>



[**Return**](#-overview)

---
