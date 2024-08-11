<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" alt="project-logo">
</p>
<p align="center">
    <h1 align="center">FMP-PY</h1>
</p>
<p align="center">
    <em>Empowering Financial Insights Through Python Simplicity</em>
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

The `fmp-py` project provides a comprehensive Python interface for accessing and analyzing financial data through the [Financial Modeling Prep (FMP) API](https://site.financialmodelingprep.com/). It offers an extensive suite of functionalities, including retrieving historical stock data, financial statements, company information, earnings, dividends, price targets, and analyst ratings. By centralizing and streamlining API interactions, `fmp-py` allows users to efficiently perform in-depth financial analysis, making it an invaluable tool for investors, analysts, and developers seeking reliable and detailed market data for informed decision-making and analysis.

[Documentation](https://fmp-py.readthedocs.io/en/latest/index.html)

---

##  Features

|    |   Feature         | Description |
|----|-------------------|---------------------------------------------------------------|
| ⚙️  | **Architecture**  | The project follows a modular architecture, organizing financial data retrieval and manipulation around core modules and models, ensuring extensibility and maintainability. |
| 🔩 | **Code Quality**  | Adopts clean coding practices with a focus on reusability and readability. Utilizes Python's type hinting and follows PEP8 guidelines. |
| 📄 | **Documentation** | Documentation is extensive, including a detailed `README.md` and module-specific docstrings. Sphinx is used for generating comprehensive HTML documentation. |
| 🔌 | **Integrations**  | Integrates seamlessly with various data sources from the Financial Modeling Prep API. Utilizes GitHub Actions for continuous integration and requests-cache for efficient API retrieval. |
| 🧩 | **Modularity**    | Highly modular with well-defined classes and methods, promoting reusability and ease of maintenance. Key functionalities are encapsulated within specific modules. |
| 🧪 | **Testing**       | Employs GitHub Actions for continuous integration. Uses requests-mock for API interaction testing, enhancing the robustness of the codebase. |
| ⚡️  | **Performance**   | Efficient data retrieval and minimal latency due to the use of requests-cache. Suitable for handling large volumes of financial data with minimal resource overhead. |
| 🛡️ | **Security**      | Sensible handling of API keys and sensitive data. Incorporates session setup with retry logic to manage API rate limits and ensure data integrity. |
| 📦 | **Dependencies**  | Key dependencies include `requests`, `requests-cache`, `pendulum`, `pandas`, `python-dotenv`, and various Sphinx modules for documentation. Utilizes `poetry` for dependency management. |
| 🚀 | **Scalability**   | Modular architecture and efficient use of caching mechanisms enable the project to scale well with increasing data loads and API calls. |

---

##  Repository Structure

```sh
└── fmp-py/
    ├── src
    │   └── fmp_py
    │       ├── __init__.py
    │       ├── fmp_base.py
    │       ├── fmp_chart_data.py
    │       ├── fmp_company_information.py
    │       ├── fmp_company_search.py
    │       ├── fmp_dividends.py
    │       ├── fmp_earnings.py
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
        ├── test_fmp_chart_data.py
        ├── test_fmp_company_information.py
        ├── test_fmp_company_search.py
        ├── test_fmp_dividends.py
        ├── test_fmp_earnings.py
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

| File                                                                               | Summary                                                                                                                                                                                                                                                             |
| ---                                                                                | ---                                                                                                                                                                                                                                                                 |
| [pyproject.toml](https://github.com/TexasCoding/fmp-py/blob/master/pyproject.toml) | Defines the projects metadata, dependencies, and configuration for the poetry package manager, ensuring streamlined installation, testing, development, and documentation processes for the `fmp-py` package which interfaces with the Financial Modeling Prep API. |

</details>

<details closed><summary>src.fmp_py</summary>

| File                                                                                                                    | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---                                                                                                                     | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [fmp_upgrades_downgrades.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_upgrades_downgrades.py)   | Provide methods to retrieve financial upgrade and downgrade data, including consensus ratings, company-specific gradings, and RSS feed updates. Essential for tracking changes in stock analyst ratings, enabling comprehensive analysis within the broader Financial Modeling Prep API integration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [fmp_financial_statements.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_financial_statements.py) | Summary of `fmp_base.py` in the `fmp-py` RepositoryThe `fmp_base.py` file serves as a foundational module within the `fmp-py` repository. This repository is aimed at providing a comprehensive Python interface for financial data access and analysis. The primary purpose of `fmp_base.py` is to establish core functionalities and base classes upon which other modules in the `src/fmp_py` directory build their specialized features. Critical features of this base module include handling requests, managing API interactions, and ensuring consistent data retrieval methods. By centralizing these core operations, `fmp_base.py` promotes code reuse, simplifies maintenance, and enhances the overall robustness of the repositorys architecture.                                                                                                                                                                                                                                                                                                                                                          |
| [fmp_chart_data.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_chart_data.py)                     | SummaryThe file in question primarily contributes to the data handling and analysis capabilities of the `fmp-py` repository, which is designed to interact with financial market data. Positioned under the `src/fmp_py` directory, this file encapsulates a specific aspect of financial data processing, such as historical data, company information, or financial statements. It integrates seamlessly with other components (like `fmp_base.py` and `fmp_financial_statements.py`) to provide a comprehensive suite for fetching, processing, and analyzing financial metrics. This functionality is critical for users who need accessible, programmatically manipulable financial data for various analytical and decision-making purposes.                                                                                                                                                                                                                                                                                                                                                                       |
| [fmp_company_search.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_company_search.py)             | FmpCompanySearch class enables comprehensive company searches using various identifiers like ISIN, CUSIP, and CIK, as well as name and ticker queries. This functionality enriches the fmp-py repository by providing extensive search capabilities for financial data, facilitating precise and flexible company information retrieval from Financial Modeling Prep (FMP).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [fmp_historical_data.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_historical_data.py)           | Facilitates retrieval of historical stock data, including daily and intraday prices, while ensuring accurate data preparation and validation within the Financial Modeling Prep (FMP) library, contributing to comprehensive financial analysis and insights in the parent repository.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [fmp_quote.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_quote.py)                               | Summary of `fmp_company_search.py`The `fmp_company_search.py` module within the `fmp-py` repository focuses on enabling users to search for company information through the Financial Modeling Prep API. This file serves as a key interface for retrieving and processing data related to company searches, including filtering and fetching relevant details about companies. This is integral to the parent repositorys architecture, which aims to provide a comprehensive Python package for interacting with various financial data endpoints from the Financial Modeling Prep service. Critical features of this module contribute to the repository's goal of offering accessible and organized financial information.                                                                                                                                                                                                                                                                                                                                                                                           |
| [fmp_statement_analysis.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_statement_analysis.py)     | Fmp_financial_statements.py`****Purpose:** The `fmp_financial_statements.py` file is designed to facilitate interactions with financial statement data, providing functionality for retrieving and processing various types of financial reports related to companies.**Critical Features:**-**Data RetrievalThe file contains mechanisms to fetch income statements, balance sheets, and cash flow statements from an external data provider.-**Data ProcessingIt includes functions to parse and organize the retrieved data for easier consumption by other parts of the application.-**API IntegrationThis file acts as a bridge between the external financial data API and the internal data structures used within the `fmp_py` project.**Relation to Parent Repository:**The `fmp_financial_statements.py` file is a crucial component in the `fmp_py` module, which lies at the core of the repositorys functionality. It enables users to access and handle financial statement data, which is essential for financial analysis, reporting, and decision-making processes supported by the broader repository. |
| [fmp_company_information.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_company_information.py)   | The `fmp_company_search.py` file within the `fmp-py` repository serves a crucial role in providing functionality for searching and retrieving company information from Financial Modeling Prep (FMP) data. Part of the broader `fmp_py` module located under the `src` directory, this specific file likely handles the logic and interfaces required to query the FMP API for company data based on various search criteria. By integrating this file into the repository, the system enables users to efficiently access and incorporate comprehensive company details into their financial analysis and modeling workflows, thus enhancing the overall utility of the `fmp-py` package.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [fmp_valuation.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_valuation.py)                       | Summary of `fmp_company_information.py` in the `fmp-py` RepositoryThe `fmp_company_information.py` file is integral to the `fmp-py` repository, which appears to be a comprehensive Python library for interfacing with financial market data. This file specifically handles the retrieval and processing of detailed company information. Key features of this module include fetching fundamental data, corporate profiles, and essential metrics that describe a companys financial health and operational status. By encapsulating these functionalities, `fmp_company_information.py` supports the broader goal of the repository to provide users with streamlined, programmatic access to diverse financial data, enhancing their ability to perform in-depth market analysis and drive informed investment decisions.                                                                                                                                                                                                                                                                                           |
| [fmp_earnings.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_earnings.py)                         | Retrieve and process earnings data from the Financial Modeling Prep API, providing functionalities like earnings surprises, confirmed earnings, earnings calendar, historical earnings, and predictions for earnings within a specified number of weeks. Enhance the repositorys capability to analyze corporate financial performance comprehensively.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [fmp_base.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_base.py)                                 | Establishes a robust base class for interacting with the Financial Modeling Prep API. Handles API key management, session setup with retry logic, and provides utility methods for data cleansing and HTTP GET requests, ensuring reliability and clean responses in the broader context of financial data retrieval and manipulation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [fmp_stock_list.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_stock_list.py)                     | Facilitates the retrieval of stock-related data from the Financial Modeling Prep API by providing methods to obtain comprehensive lists and details of stocks, ETFs, indexes, symbols, and reports. Integrates seamlessly with the repositorys architecture, enhancing its data access capabilities for financial markets.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [fmp_price_targets.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_price_targets.py)               | Provide methods to retrieve price target data from the Financial Modeling Prep API, including consensus, summary, and detailed targets. Facilitates structured and clear access to price target information for stock symbols, enhancing financial analysis capabilities within the repositorys data retrieval architecture.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [fmp_dividends.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_dividends.py)                       | The `fmp_dividends` module facilitates the retrieval of dividends information by providing functions to access dividends calendar data within a specified date range and historical dividends data for particular stock symbols, contributing to the repositorys goal of delivering comprehensive financial modeling capabilities.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

</details>

<details closed><summary>src.fmp_py.models</summary>

| File                                                                                                                 | Summary                                                                                                                                                                                                                                                                                                                                                                                |
| ---                                                                                                                  | ---                                                                                                                                                                                                                                                                                                                                                                                    |
| [price_targets.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/models/price_targets.py)             | Models price target data for financial assets by defining structures for consensus and summary information, crucial for aggregating analysts price target estimates and historical price target trends. Enhances the repositorys capability to provide comprehensive financial insights related to asset price projections.                                                            |
| [statement_analysis.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/models/statement_analysis.py)   | Define the data structures necessary for financial statement analysis, encompassing financial scores, key metrics, and various ratios. These structures support comprehensive financial evaluations, facilitating the broader repositorys goal of providing detailed financial data analysis and insights for various financial instruments and companies.                             |
| [company_information.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/models/company_information.py) | Defines data structures related to company information critical for representing stock peers, core company attributes, market capitalization, executive compensation details, and comprehensive company profiles. Facilitates handling and organization of company data within the repositorys architecture, enabling streamlined data access and manipulation across various modules. |
| [quote.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/models/quote.py)                             | Models various types of financial quotes including real-time, forex, crypto, and aftermarket data. Supports detailed attributes for financial instruments, contributing to the repositorys ability to handle diverse financial data integrations and enabling accurate and comprehensive financial analysis within the broader architecture.                                           |
| [upgrades_downgrades.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/models/upgrades_downgrades.py) | Define a data model for storing and managing stock upgrade and downgrade ratings, encapsulating various rating counts and consensus information. This model plays a crucial role in organizing and standardizing financial data, enabling other components in the repository to effectively process and analyze stock ratings.                                                         |
| [valuation.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/models/valuation.py)                     | Define data structures for storing valuation metrics, including discounted cash flow and company ratings, which are integral to analyzing financial health within the repositorys financial modeling framework. These structures facilitate the seamless integration of valuation data into the broader analytics capabilities of the project.                                         |

</details>

<details closed><summary>.github.workflows</summary>

| File                                                                                                       | Summary                                                                                                                                                                                                                                                                                                                                                |
| ---                                                                                                        | ---                                                                                                                                                                                                                                                                                                                                                    |
| [test-package.yaml](https://github.com/TexasCoding/fmp-py/blob/master/.github/workflows/test-package.yaml) | Defines a GitHub Actions workflow for automated testing, ensuring continuous integration. Executes tests on each push and pull request to maintain code quality and functionality within the repository. Integrates seamlessly with the existing test suite and configuration specified in the tests directory, reinforcing overall project stability. |

</details>

---

##  Getting Started

**System Requirements:**

* **Python**: `version >=3.10`

###  Installation

<h4>From <code>source</code></h4>

> 1. Clone the fmp-py repository:
>
> ```console
> $ git clone https://github.com/TexasCoding/fmp-py
> ```
>
> 2. Change to the project directory:
> ```console
> $ cd fmp-py
> ```
>
> 3. Install the dependencies:
> ```console
> $ poetry install
> ```

###  Usage

<h4>From <code>source</code></h4>

> Run fmp-py using the command below:
> ```console
> $ python main.py
> ```

###  Tests

> Run the test suite using the command below:
> ```console
> $ pytest
> ```

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
