<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" alt="project-logo">
</p>
<p align="center">
    <h1 align="center">FMP-PY</h1>
</p>
<p align="center">
    <em>Empower Your Financial Insights with Precision Data</em>
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

The fmp-py project is a comprehensive Python library designed for seamless interaction with the [Financial Modeling Prep (FMP) API](https://site.financialmodelingprep.com/), enabling users to retrieve and analyze a wide range of financial data. Its core functionalities include company searches, fetching historical and real-time stock data, and conducting financial statement analysis. By providing structured data representations and facilitating data retrieval through a robust API integration, fmp-py empowers financial analysts, developers, and researchers to access reliable and detailed market insights efficiently, making it an invaluable tool for financial data analysis and decision-making.

---

##  Features

|    | Feature         | Description |
|----|-------------------|---------------------------------------------------------------|
| ⚙️  | **Architecture**  | The project follows a modular architecture with separate components for different financial data functionalities, including company search, historical data, and quotes. It leverages Python's object-oriented principles for structured data interaction. |
| 🔩 | **Code Quality**  | The codebase adheres to standard Python coding conventions and best practices, with a focus on readability and maintainability. Tools like `pre-commit` and `ruff` are used to ensure code quality. |
| 📄 | **Documentation** | The project includes comprehensive documentation generated using `sphinx` and `sphinx-rtd-theme`, covering API usage, installation, and examples. However, some modules could benefit from more detailed docstrings. |
| 🔌 | **Integrations**  | Key integrations include the Financial Modeling Prep (FMP) API for financial data retrieval. The project also integrates with `pandas` for data handling and `requests` for HTTP requests. |
| 🧩 | **Modularity**    | The codebase is highly modular with discrete files for different functionalities like company search, historical data, and quotes. Each module can be reused independently or integrated into larger workflows. |
| 🧪 | **Testing**       | The project uses `pytest` for testing, with test automation handled through GitHub Actions (`.github/workflows/test-package.yaml`). It includes mock testing of API requests using `requests-mock`. |
| ⚡️  | **Performance**   | The performance is optimized for efficiency in data retrieval and processing. The use of `pandas` ensures fast data manipulation, while caching mechanisms could be implemented for further improvements. |
| 🛡️ | **Security**      | Security measures include API key management via environment variables using `python-dotenv`. There are no explicit details on data encryption or access control within the provided information. |
| 📦 | **Dependencies**  | Key dependencies include `pandas`, `requests`, `python-dotenv`, `pendulum`, and documentation tools like `sphinx`, `myst-parser`, and `nbsphinx`. Dependency management is handled via `pyproject.toml` with Poetry. |

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
    │       ├── fmp_historical_data.py
    │       ├── fmp_quote.py
    │       ├── fmp_statement_analysis.py
    │       ├── fmp_stock_list.py
    │       └── models
    │           ├── company_information.py
    │           ├── quote.py
    │           └── statement_analysis.py
    └── tests
        ├── __init__.py
        ├── test_fmp_company_information.py
        ├── test_fmp_company_search.py
        ├── test_fmp_historical_data.py
        ├── test_fmp_quote.py
        ├── test_fmp_statement_analysis.py
        └── test_fmp_stock_list.py
```

---

##  Modules

<details closed><summary>.</summary>

| File                                                                               | Summary                                                                                                                                                                                                                                                                                                   |
| ---                                                                                | ---                                                                                                                                                                                                                                                                                                       |
| [pyproject.toml](https://github.com/TexasCoding/fmp-py/blob/master/pyproject.toml) | Defines the project metadata, dependencies, and configuration settings for packaging and managing the repository using Poetry. Facilitates streamlined dependency management, testing, and documentation generation within the project architecture, ensuring consistent development and build processes. |

</details>

<details closed><summary>src.fmp_py</summary>

| File                                                                                                                  | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ---                                                                                                                   | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [fmp_company_search.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_company_search.py)           | Facilitates searching for companies on Financial Modeling Prep (FMP) through various identifiers like ISIN, CUSIP, CIK, and ticker symbols. Provides multiple search methods to retrieve detailed information about companies, ensuring compatibility with various stock exchanges and delivering results in a structured data format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [fmp_historical_data.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_historical_data.py)         | Retrieve and process historical and intraday price data for financial assets, leveraging the Financial Modeling Prep API. Provide functionalities to clean, calculate VWAP, and format the data, ensuring accurate and usable historical financial data within the fmp-py librarys architecture.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [fmp_quote.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_quote.py)                             | Facilitating requests to external financial data APIs to fetch historical data.-Parsing and structuring the acquired data into a usable format for further analysis or visualization.-Ensuring consistency and reliability in the data retrieval process, contributing to the overall robustness of the `fmp-py` package.In the context of the repository, `fmp_historical_data.py` plays a vital role in offering comprehensive financial insights, complementing other modules that focus on company information, stock lists, and financial statements.                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [fmp_statement_analysis.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_statement_analysis.py)   | Fmp_py/fmp_quote.py Summary**Main Purpose:** The `fmp_quote.py` file within the `fmp-py` repository is designed to provide functionalities for fetching and handling real-time stock quotes. It serves as a crucial component in accessing up-to-date financial market data.**Critical Features:**-**Fetch Real-Time Quotes:** Retrieves current stock prices and related information.-**Data Processing:** Handles the formatting and basic processing of stock quote data.-**Integration:** Seamlessly integrates with other modules like `fmp_company_information` and `fmp_historical_data` to provide a comprehensive financial data toolkit.In the context of the parent repository's architecture, `fmp_quote.py` is essential for enabling real-time financial data access, which is fundamental for users needing up-to-date market insights.---This summary highlights the main purpose and features of `fmp_quote.py` without diving into technical implementation details. |
| [fmp_company_information.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_company_information.py) | Sure, please provide the code file for which the summary should be generated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [fmp_base.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_base.py)                               | Facilitates interaction with the Financial Modeling Prep API by handling API key management, session establishment, and GET requests, ensuring seamless data retrieval and response parsing across various endpoints in the repository. Functions as the foundational class for API communication within the broader architecture of the project.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [fmp_stock_list.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_stock_list.py)                   | Provides a comprehensive interface for retrieving various stock and financial data from the Financial Modeling Prep API, including stock lists, exchange-traded funds, financial statement symbols, and stock symbols for specific exchanges. Ensures data is organized and returned as pandas DataFrames for seamless integration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

</details>

<details closed><summary>src.fmp_py.models</summary>

| File                                                                                                                 | Summary                                                                                                                                                                                                                                                                                                                                                                            |
| ---                                                                                                                  | ---                                                                                                                                                                                                                                                                                                                                                                                |
| [statement_analysis.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/models/statement_analysis.py)   | Provide a structured representation of financial data, including financial scores, ratios, and key metrics, essential for performing in-depth company financial analysis within the broader functionality of the repository.                                                                                                                                                       |
| [company_information.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/models/company_information.py) | Define essential data structures for company information, encompassing core details, market capitalization, executive compensation, company profile, and stock peers. Facilitate organized and comprehensive representation of company-related data within the repositorys architecture for efficient data manipulation and retrieval.                                             |
| [quote.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/models/quote.py)                             | Define data structures for various types of financial quotes, including stocks, forex, cryptocurrencies, and aftermarket trades, facilitating consistent data representation across the repositorys architecture. These models support type checking and serialization, ensuring robust and efficient data handling within the broader financial market data processing framework. |

</details>

<details closed><summary>.github.workflows</summary>

| File                                                                                                       | Summary                                                                                                                                                   |
| ---                                                                                                        | ---                                                                                                                                                       |
| [test-package.yaml](https://github.com/TexasCoding/fmp-py/blob/master/.github/workflows/test-package.yaml) | Establishes continuous integration by automating tests for the repository using GitHub Actions, ensuring code quality and functionality with each update. |

</details>


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
