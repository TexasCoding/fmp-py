<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" alt="project-logo">
</p>
<p align="center">
    <h1 align="center">FMP-PY</h1>
</p>
<p align="center">
    <em>Empower Your Financial Insights with Seamless FMP API Integration</em>
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

The fmp-py project is a Python package designed to interface seamlessly with the [Financial Modeling Prep (FMP) API](https://site.financialmodelingprep.com/), providing robust functionality for financial data retrieval and analysis. It features modules for obtaining stock upgrades and downgrades, company profiles, financial statements, historical and intraday market data, price targets, and comprehensive valuation metrics. By centralizing diverse financial data in a structured and accessible manner, fmp-py enables users to perform in-depth financial analysis, aiding informed decision-making and enhancing the efficiency of financial research and reporting activities. Its cohesive design ensures consistency and ease of use across various financial data needs.

---

##  Features

|    |   Feature         | Description |
|----|-------------------|---------------------------------------------------------------|
| ⚙️  | **Architecture**  | The project follows a modular structure, segregating functionalities across multiple Python modules. It leverages the Financial Modeling Prep API to retrieve and manipulate financial data. |
| 🔩 | **Code Quality**  | The repository's code adheres to standard Python code styles, utilizing tools like `ruff` for linting, ensuring readability, and maintainability. |
| 📄 | **Documentation** | The project is well-documented using Sphinx, which offers comprehensive API documentation and usage examples, facilitating ease of understanding for new contributors. |
| 🔌 | **Integrations**  | Integrates with Financial Modeling Prep API for data retrieval and GitHub Actions for continuous integration and testing. External tools like Poetry manage dependencies. |
| 🧩 | **Modularity**    | The codebase is highly modular, with distinct modules for various financial data operations like company search, historical data, and financial statements, promoting reusability and ease of maintenance. |
| 🧪 | **Testing**       | The project employs `requests-mock` for mocking API calls and GitHub Actions for continuous integration, ensuring robust and reliable test coverage. |
| ⚡️ | **Performance**   | Performance details are not explicitly discussed, but given its API-based architecture, efficiency largely relies on the Financial Modeling Prep API's response time and the effective use of data manipulation libraries like `pandas`. |
| 🛡️ | **Security**      | API key management is handled securely through environmental variables, ensuring sensitive data such as API keys are not hard-coded. No explicit mention of further security measures. |
| 📦 | **Dependencies**  | Key dependencies include `python-dotenv`, `sphinx`, `requests`, `ruff`, `requests-mock`, `pandas`, `pendulum`, `pre-commit`, and `sphinx-rtd-theme`. |
| 🚀 | **Scalability**   | The project's modularity and reliance on external APIs imply it can scale with increased data volume and complexity, provided the external API can handle the load. |

---

##  Repository Structure

```sh
└── fmp-py/
    ├── .github
    │   ├── ISSUE_TEMPLATE
    │   │   ├── bug_report.md
    │   │   ├── custom.md
    │   │   └── feature_request.md
    │   └── workflows
    │       └── test-package.yaml
    ├── CODE_OF_CONDUCT.md
    ├── LICENSE
    ├── README.md
    ├── SECURITY.md
    ├── docs
    │   ├── Makefile
    │   ├── make.bat
    │   ├── rtd_requirements.txt
    │   └── source
    │       ├── conf.py
    │       └── index.md
    ├── poetry.lock
    ├── pyproject.toml
    ├── pytest.ini
    ├── src
    │   └── fmp_py
    │       ├── __init__.py
    │       ├── fmp_base.py
    │       ├── fmp_company_information.py
    │       ├── fmp_company_search.py
    │       ├── fmp_financial_statements.py
    │       ├── fmp_historical_data.py
    │       ├── fmp_price_targets.py
    │       ├── fmp_quote.py
    │       ├── fmp_statement_analysis.py
    │       ├── fmp_stock_list.py
    │       ├── fmp_upgrades_downgrades.py
    │       ├── fmp_valuation.py
    │       └── models
    │           ├── company_information.py
    │           ├── price_targets.py
    │           ├── quote.py
    │           ├── statement_analysis.py
    │           ├── upgrades_downgrades.py
    │           └── valuation.py
    └── tests
        ├── __init__.py
        ├── test_fmp_company_information.py
        ├── test_fmp_company_search.py
        ├── test_fmp_financial_statements.py
        ├── test_fmp_historical_data.py
        ├── test_fmp_price_targets.py
        ├── test_fmp_quote.py
        ├── test_fmp_statement_analysis.py
        ├── test_fmp_stock_list.py
        ├── test_fmp_upgrades_downgrades.py
        └── test_fmp_valuation.py
```

---

##  Modules

<details closed><summary>.</summary>

| File                                                                               | Summary                                                                                                                                                                                                                                                                                                                                                       |
| ---                                                                                | ---                                                                                                                                                                                                                                                                                                                                                           |
| [pyproject.toml](https://github.com/TexasCoding/fmp-py/blob/master/pyproject.toml) | Define project metadata and dependencies for the Python package fmp-py. Establish essential configurations for tools like Poetry, Ruff, and Sphinx, streamlining development, testing, documentation, and dependency management. Centralize settings, ensuring consistency across various environments and facilitating smooth project setup and maintenance. |

</details>

<details closed><summary>src.fmp_py</summary>

| File                                                                                                                    | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---                                                                                                                     | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [fmp_upgrades_downgrades.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_upgrades_downgrades.py)   | Provide methods for retrieving stock upgrade and downgrade data from the Financial Modeling Prep API, focusing on individual symbols, company-specific data, and RSS feeds. Enable the analysis of stock performance metrics such as consensus ratings and historical grading, enhancing financial decision-making capabilities within the repository architecture.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [fmp_financial_statements.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_financial_statements.py) | Summary for `fmp_company_information.py`The `fmp_company_information.py` file within the `fmp-py` repository is responsible for handling the retrieval and management of company-related information. This module serves as a fundamental component in fetching detailed company data such as profiles, key metrics, and other essential informational attributes from the external source it interfaces with. The functionality it provides is pivotal for users who need comprehensive company information for analysis, reporting, or integration into broader financial systems. It integrates seamlessly with other modules in the `src/fmp_py` directory to offer a holistic approach to financial data processing within the repositorys architecture.                                                                                                                                                                                                                                                         |
| [fmp_company_search.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_company_search.py)             | Facilitates company searches on Financial Modeling Prep by providing various methods such as ISIN, CUSIP, CIK, company name, and ticker searches. Converts search results into structured DataFrames, assisting users in accessing detailed company information efficiently within the repositorys data retrieval architecture.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [fmp_historical_data.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_historical_data.py)           | Facilitates retrieval and preparation of historical and intraday market data for financial assets by integrating with the Financial Modeling Prep API. Provides essential data manipulation functionalities like VWAP calculation and price rounding, ensuring data consistency and usability within the repositorys broader framework for financial analysis.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [fmp_quote.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_quote.py)                               | Summary of `fmp_company_search.py`The `fmp_company_search.py` file is part of the `fmp-py` repository, which appears to be a Python package designed to interact with financial data. This specific file focuses on enabling users to search for company information, likely by querying a financial database or API. It plays a critical role in the parent repositorys architecture by providing essential functionality for identifying and retrieving details on companies, which can be used in various financial analyses or reporting tools available in the package. This feature complements the other modules, such as financial statements and historical data management, to offer a comprehensive toolkit for financial data analysis.                                                                                                                                                                                                                                                                   |
| [fmp_statement_analysis.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_statement_analysis.py)     | The `fmp_company_information.py` file within the `fmp-py` repository serves as a crucial module that provides functionalities to retrieve and manage company-related data. It operates as a key component of the `fmp_py` package, integrating with other modules to offer comprehensive financial data services. This file specifically focuses on fetching detailed company information essential for users aiming to perform in-depth financial analysis and research. It complements other modules in the repository, such as those handling financial statements, historical data, and stock valuations, to create a robust financial data analysis toolset.                                                                                                                                                                                                                                                                                                                                                     |
| [fmp_company_information.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_company_information.py)   | The `fmp_company_search.py` file within the `fmp-py` repository is dedicated to handling operations related to searching for company information using the Financial Modeling Prep (FMP) API. This file is a crucial component of the repositorys architecture, enabling users to query and retrieve detailed data about various companies, such as their names, symbols, and other identifiers. It plays an essential role in providing an interface for accessing and filtering company data, thereby supporting the broader objective of the repository which is to facilitate financial data retrieval and analysis through an organized and accessible set of API endpoints and models.                                                                                                                                                                                                                                                                                                                          |
| [fmp_valuation.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_valuation.py)                       | Summary of `fmp_company_information.py`The `fmp_company_information.py` file is a part of the `fmp-py` repository, which is structured to provide various functionalities related to financial market data through Python modules. The primary purpose of this specific file is to handle the retrieval and processing of detailed company information. This module interacts with external data sources to gather comprehensive company data, which can then be utilized by other modules or directly by users for financial analysis and decision-making.In the context of the repositorys architecture, this file is crucial for ensuring that accurate and updated company-specific information is available, thereby supporting the broader goal of offering a robust financial market data toolkit. The data managed by this module includes company profiles, key financial metrics, and other relevant corporate information that is essential for users conducting thorough financial research and analysis. |
| [fmp_base.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_base.py)                                 | Facilitates core API interaction for the Financial Modeling Prep library by managing API key authentication, making GET requests, and parsing JSON responses. Provides utility functions to clean and convert data types and ensures proper session management. Central to all API-related functionalities in the repository.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [fmp_stock_list.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_stock_list.py)                     | FmpStockList class interacts with the Financial Modeling Prep API to retrieve various lists of stocks, ETFs, indexes, and exchange symbols. It provides essential stock market data and updates, aiding users in comprehensive financial analysis and decision-making within the broader repository architecture.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [fmp_price_targets.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_price_targets.py)               | Retrieve and organize price target data for stocks from the Financial Modeling Prep API, including detailed summaries, consensus figures, and historical targets, presented in a structured DataFrame format. This enhances the repositorys capabilities for comprehensive financial analysis and target assessments.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

</details>

<details closed><summary>src.fmp_py.models</summary>

| File                                                                                                                 | Summary                                                                                                                                                                                                                                                                                                                                                            |
| ---                                                                                                                  | ---                                                                                                                                                                                                                                                                                                                                                                |
| [price_targets.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/models/price_targets.py)             | Defines data structures for organizing and representing stock price target information, aiding in the retrieval and analysis of price targets across different timeframes. Facilitates structured storage of high, low, consensus, and median targets, enhancing the parent repositorys capability to handle detailed financial data.                              |
| [statement_analysis.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/models/statement_analysis.py)   | Define data models for key financial metrics and scores used in analyzing a companys financial health, including ratios and key performance indicators. These models standardize the representation of financial data, facilitating efficient data manipulation and integration within the broader financial analysis functionalities of the fmp-py repository.    |
| [company_information.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/models/company_information.py) | Defines data models representing various aspects of company information, including stock peers, core details, market capitalization, executive compensation, and company profiles. These models are integral to structuring and managing financial data within the repository, facilitating efficient data handling and interaction across different modules.      |
| [quote.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/models/quote.py)                             | Define data structures for various types of market quotes and pricing information, including stocks, forex, crypto, aftermarket data, and price changes, supporting the repositorys functionality for comprehensive financial market data retrieval and analysis.                                                                                                  |
| [upgrades_downgrades.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/models/upgrades_downgrades.py) | Models and manages data for stock analyst ratings, capturing the number of recommendations by type (strong buy, buy, hold, sell, and strong sell) and consensus. Integrates into the broader functionality of the repository, which focuses on financial market analysis and predictions.                                                                          |
| [valuation.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/models/valuation.py)                     | Define data structures to model discounted cash flow and company ratings, enabling accurate financial analysis and valuation within the repository. Standardize financial data representation to support various valuation methods and company performance assessments, aligning with the overarching goal of providing comprehensive financial market data tools. |

</details>

<details closed><summary>.github.workflows</summary>

| File                                                                                                       | Summary                                                                                                                                                                                                                                                                                                                          |
| ---                                                                                                        | ---                                                                                                                                                                                                                                                                                                                              |
| [test-package.yaml](https://github.com/TexasCoding/fmp-py/blob/master/.github/workflows/test-package.yaml) | Automates continuous integration by defining the workflow for running tests. Ensures code quality and stability in the repository through systematic testing. Integrates with GitHub Actions to trigger tests upon code changes, reinforcing the reliability of the package by catching issues early in the development process. |

</details>

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://github.com/TexasCoding/fmp-py/issues)**: Submit bugs found or log feature requests for the `fmp-py` project.
- **[Submit Pull Requests](https://github.com/TexasCoding/fmp-py/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/TexasCoding/fmp-py/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/TexasCoding/fmp-py
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="center">
   <a href="https://github.com{/TexasCoding/fmp-py/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=TexasCoding/fmp-py">
   </a>
</p>
</details>

---

##  License

This project is protected under the [MIT](https://github.com/TexasCoding/fmp-py?tab=MIT-1-ov-file) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/mit/) file.


[**Return**](#-overview)

---
