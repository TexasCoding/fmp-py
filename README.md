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

### This project is under development, please check back later for updates.

##  Overview

The fmp-py project is an open-source Python library designed to aggregate and manage comprehensive financial data from [Financial Modeling Prep (FMP) API](https://site.financialmodelingprep.com/). It offers robust functionalities including company searches, retrieval of financial statements, stock price data, price targets, and detailed company information. By integrating seamlessly with the FMP API, fmp-py provides a user-friendly interface for querying and analyzing financial data, supporting diverse search parameters and historical data analysis. This modular and well-organized codebase ensures efficient data handling, making fmp-py a valuable tool for financial analysts and developers seeking streamlined access to financial market insights.

---

##  Features

|    |   Feature         | Description |
|----|-------------------|---------------------------------------------------------------|
| ⚙️  | **Architecture**  | The project features a modular design, with self-contained modules targeting different aspects of financial data processing, ensuring maintainability and scalability. |
| 🔩 | **Code Quality**  | Code adheres to consistent style and format, supported by Ruff integration for code quality and format adherence, and automated testing through GitHub Actions. |
| 📄 | **Documentation** | Comprehensive documentation is available for modules, detailing their purpose and key features. Sphinx is used for generating documentation, ensuring high quality and consistency. |
| 🔌 | **Integrations**  | Integrates with the Financial Modeling Prep API to retrieve comprehensive financial data. Includes dependencies like requests, pandas, and various Sphinx extensions. |
| 🧩 | **Modularity**    | Highly modular with each file representing a specific aspect of financial data, promoting reusability and ease of maintenance. Standardized interfaces across modules enhance usability. |
| 🧪 | **Testing**       | Employs automated testing workflows via GitHub Actions. Uses requests-mock for API interaction testing, ensuring robust and reliable code. |
| ⚡️  | **Performance**   | Efficient data retrieval and processing mechanisms in place. Utilizes pandas for data manipulation, ensuring high-speed operations and minimal resource usage. |
| 🛡️ | **Security**      | Uses dotenv for managing environment variables and API keys securely. Ensures data is correctly sanitized and validated before processing. |
| 📦 | **Dependencies**  | Key dependencies include requests, pandas, python-dotenv, Sphinx, and poetry for package management. These libraries are essential for API interaction, data handling, and documentation. |
| 🚀 | **Scalability**   | Designed to handle large volumes of financial data. Modular architecture and efficient data processing ensure it can scale with increased data input and user demand. |

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
    │       ├── fmp_valuation.py
    │       └── models
    │           ├── company_information.py
    │           ├── price_targets.py
    │           ├── quote.py
    │           ├── statement_analysis.py
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
        └── test_fmp_valuation.py
```

---

##  Modules

<details closed><summary>.</summary>

| File                                                                               | Summary                                                                                                                                                                                                                                                                                                                                                 |
| ---                                                                                | ---                                                                                                                                                                                                                                                                                                                                                     |
| [pyproject.toml](https://github.com/TexasCoding/fmp-py/blob/master/pyproject.toml) | Define project metadata, dependencies, and build configurations using Poetry. Enable robust dependency management and streamline project setup for contributors and users. Facilitate consistent development, testing, and documentation standards across the `fmp-py` repository. Optimize code quality and format adherence through Ruff integration. |

</details>

<details closed><summary>src.fmp_py</summary>

| File                                                                                                                    | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ---                                                                                                                     | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [fmp_financial_statements.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_financial_statements.py) | Company Search FunctionalityEnables detailed searching for company information using various parameters.2. **Integration with FMP APISeamlessly connects to the Financial Modeling Prep services to fetch and return relevant company data.3. **User-Friendly InterfaceDesigned to be intuitive and easy to use, aligning with the repository’s goal of providing accessible financial data management and retrieval tools.This module complements other components like `fmp_financial_statements.py` and `fmp_quote.py`, together forming a cohesive toolkit for comprehensive financial data analysis and operations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [fmp_company_search.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_company_search.py)             | Enable comprehensive company searches on Financial Modeling Prep using various identifiers like ISIN, CUSIP, and CIK, as well as by name, ticker, or general query. Facilitate robust querying capabilities and streamline retrieval of detailed company information, supporting diverse search parameters and filters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [fmp_historical_data.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_historical_data.py)           | Facilitate the retrieval of both daily and intraday historical stock price data, with functionality to prepare and format this data, including calculating the Volume Weighted Average Price (VWAP). Integrate with Financial Modeling Prep API and handle various time intervals and date ranges for comprehensive historical data analysis.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [fmp_quote.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_quote.py)                               | Fmp_company_information.py`****Purpose:**The `fmp_company_information.py` file is a critical component within the `src/fmp_py` directory of the `fmp-py` repository. Its main purpose is to facilitate the retrieval and management of company-related information from the underlying financial market APIs integrated within the `fmp-py` package.**Critical Features:**-**Data Retrieval:** Provides functionalities to fetch comprehensive company information, such as company profiles, details, and relevant metadata.-**API Integration:** Acts as an intermediary to seamlessly integrate the external financial market APIs, ensuring the data is correctly fetched and formatted.-**Information Structuring:** Organizes and structures the acquired data into a usable format for other modules and end-users within the package.By encapsulating these functionalities, `fmp_company_information.py` plays a pivotal role in the architecture of the `fmp-py` repository, enhancing its capability to deliver precise and structured company information to users.                        |
| [fmp_statement_analysis.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_statement_analysis.py)     | Fmp_company_information.py`**Purpose:**The `fmp_company_information.py` module focuses on retrieving and managing company-related data. This includes essential information about a company, such as its profile, executives, and other relevant metadata.**Critical Features:**-Defines methods for fetching detailed company profiles.-Supports functionalities to access executive profiles and other metadata.-Acts as a critical link within the parent repository for obtaining company-specific information, ensuring that users can easily access and manipulate company data.### Relation to Parent Repository:Within the architecture of the fmp-py" repository, this code serves as a specialized component responsible for handling all operations and queries related to company information. It complements other modules like `fmp_financial_statements` and `fmp_quote`, together providing a comprehensive toolkit for financial data analysis and retrieval.                                                                                                                         |
| [fmp_company_information.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_company_information.py)   | Summary for `fmp_company_information.py`:**Purpose`fmp_company_information.py` focuses on retrieving and managing company information data from the Financial Modeling Prep (FMP) API, serving as a critical module within the broader `fmp-py` library.**Key Features-**Data RetrievalFacilitates easy access to detailed company information such as profiles, management, and financial metrics.-**IntegrationSeamlessly integrates with other modules in `fmp-py` to provide comprehensive financial data analysis.-**Utility FunctionsIncludes utility functions for processing and formatting the retrieved data, ensuring consistency and usability across the `fmp-py` package.In the context of the repository's architecture, this module plays a vital role in enhancing the data richness and analytical capabilities of the `fmp-py` package, supporting both individual and interconnected functionalities.---This summary highlights the main purpose and key features of the `fmp_company_information.py` file without delving into the specific technicalities of its implementation. |
| [fmp_valuation.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_valuation.py)                       | Each file represents a self-contained module targeting a particular aspect of financial data, ensuring the codebase is modular and easy to maintain.2. **Interface ConsistencyAll modules follow a standardized interface, promoting ease of use across different financial data types.3. **Model IntegrityThe `models` sub-directory contains definitions for data structures used across various modules, ensuring consistent data handling and manipulation.By organizing the code in this manner, the repository ensures that users can easily find and utilize specific financial functionalities, promoting a robust and scalable architecture.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [fmp_base.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_base.py)                                 | Serves as the foundational component for API interactions within the repository, offering methods for initializing API access, sanitizing data types, and handling GET requests. Ensures session management and error handling for seamless integration with Financial Modeling Preps endpoints.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [fmp_stock_list.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_stock_list.py)                     | Retrieve and organize a comprehensive list of stock market data from Financial Modeling Prep API, including available indexes, exchange symbols, symbol changes, CIK list, commitment of traders report, and various other stock-related information. Provide robust data processing and error handling capabilities.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [fmp_price_targets.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_price_targets.py)               | Retrieve detailed price targets from the Financial Modeling Prep API, including consensus, summary, and individual target data. Facilitate data manipulation using Pandas and handle API interactions and error management. Integrate seamlessly within the broader architecture to enrich financial analysis capabilities for users.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

</details>

<details closed><summary>src.fmp_py.models</summary>

| File                                                                                                                 | Summary                                                                                                                                                                                                                                                                                                                                                      |
| ---                                                                                                                  | ---                                                                                                                                                                                                                                                                                                                                                          |
| [price_targets.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/models/price_targets.py)             | Defines data structures for managing and organizing price target information related to stocks. Plays a crucial role in structuring financial data for further analysis and reporting within the repository’s broader financial modeling and prediction capabilities.                                                                                        |
| [statement_analysis.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/models/statement_analysis.py)   | Define data structures essential for financial statement analysis, encapsulating financial scores, key ratios, and metrics. Facilitate the organization and retrieval of comprehensive financial data attributes, which support the repositorys goal of providing robust financial market analysis tools.                                                    |
| [company_information.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/models/company_information.py) | Define data structures for company-related information, including core details, market capitalization, executive compensation, and company profiles, enabling organized and standardized storage of this data within the parent repositorys financial market platform.                                                                                       |
| [quote.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/models/quote.py)                             | Provide data structures for various financial market quotes, including real-time prices, forex, crypto, and aftermarket trades, to encapsulate a range of financial data. Each class captures essential attributes relevant to specific market contexts, integrating seamlessly into the repositorys architecture for comprehensive financial data analysis. |
| [valuation.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/models/valuation.py)                     | Provide data structures for discounted cash flow and company ratings within the valuation module, enabling efficient storage and retrieval of financial metrics and recommendations in the parent repositorys financial model package.                                                                                                                       |

</details>

<details closed><summary>.github.workflows</summary>

| File                                                                                                       | Summary                                                                                                                                                                                                                                                                                           |
| ---                                                                                                        | ---                                                                                                                                                                                                                                                                                               |
| [test-package.yaml](https://github.com/TexasCoding/fmp-py/blob/master/.github/workflows/test-package.yaml) | Facilitates automated testing of the repository by defining workflows that run tests on code changes, ensuring code quality and functionality remain intact. Integrates with GitHub Actions to provide continuous integration and streamlined development processes through automated validation. |

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
