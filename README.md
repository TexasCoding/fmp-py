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

The fmp-py project offers a comprehensive Python interface for interacting with financial market data, integrating the [Financial Modeling Prep (FMP) API](https://site.financialmodelingprep.com/) to retrieve and analyze diverse financial datasets. It supports functionalities like accessing company information, historical stock prices, financial statements, stock lists, and upgrades/downgrades. The package provides tools for enhanced financial analysis, including data models for price targets and valuations. Its modular structure ensures seamless data retrieval and processing, making it a valuable resource for financial analysts, researchers, and developers aiming to perform in-depth market analysis and informed investment decisions.


[Documentation](https://fmp-py.readthedocs.io/en/latest/index.html)

---

##  Features

|    |   Feature         | Description |
|----|-------------------|---------------------------------------------------------------|
| ⚙️  | **Architecture**  | The project is structured as a Python package for financial data analysis. It integrates with the Financial Modeling Prep API, providing modules for various financial data aspects. |
| 🔩 | **Code Quality**  | The project uses automated tools like `pre-commit` and `ruff` for code style and quality enforcement, ensuring consistency and high standards. |
| 📄 | **Documentation** | Documentation is enhanced using `sphinx`, `myst-parser`, and `sphinx-autoapi`, indicating a focus on comprehensive and user-friendly documentation. |
| 🔌 | **Integrations**  | Key integration is with the Financial Modeling Prep API, enabling comprehensive access to various financial data points. |
| 🧩 | **Modularity**    | Codebase is highly modular, with distinct modules for different data aspects like company information, historical data, financial statements, etc., ensuring reusability. |
| 🧪 | **Testing**       | Uses `requests-mock` for API testing and GitHub Actions for CI/CD, ensuring robust testing and continuous integration. |
| ⚡️  | **Performance**   | Efficient handling and processing of financial data with modules returning results in pandas DataFrame format for speed and usability in analysis. |
| 🛡️ | **Security**      | Uses `python-dotenv` for managing sensitive data, emphasizing secure data handling practices. |
| 📦 | **Dependencies**  | Utilizes key libraries like `pandas` for data manipulation, `requests` for HTTP requests, and `pendulum` for date handling, among others. |
| 🚀 | **Scalability**   | Designed for efficiency in data retrieval and processing, though specifics on load handling are not detailed, the modular design suggests good scalability potential. |

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
    │       ├── index.md
    │       └── notebooks
    │           └── usage.ipynb
    ├── poetry.lock
    ├── pyproject.toml
    ├── pytest.ini
    ├── src
    │   └── fmp_py
    │       ├── __init__.py
    │       ├── fmp_base.py
    │       ├── fmp_charts.py
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

| File                                                                               | Summary                                                                                                                                                                                                                                                                                               |
| ---                                                                                | ---                                                                                                                                                                                                                                                                                                   |
| [pyproject.toml](https://github.com/TexasCoding/fmp-py/blob/master/pyproject.toml) | Define the projects metadata and dependencies, streamline the build and packaging processes, and set up configuration standards for development and testing. Enhance code quality and documentation through automated tools and enforce consistent coding styles and practices across the repository. |

</details>

<details closed><summary>src.fmp_py</summary>

| File                                                                                                                    | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ---                                                                                                                     | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [fmp_upgrades_downgrades.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_upgrades_downgrades.py)   | Retrieve and process stock upgrade and downgrade data from the Financial Modeling Prep API. Provide methods to access consensus data, company-specific gradings, and RSS feed updates, returning results in pandas DataFrame format for easy analysis. Enhance the repositorys capability to handle financial data comprehensively.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [fmp_financial_statements.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_financial_statements.py) | The code file `fmp_company_information.py` under the `fmp-py` repository plays a crucial role in managing and retrieving company information. It is designed to interface with external APIs or databases to fetch detailed corporate data such as governance structures, fundamental descriptions, and key financial metrics. This functionality is critical within the broader architecture of the repository, which focuses on providing comprehensive financial market data through various modules. The `fmp_company_information.py` integrates seamlessly with other components like financial statements and historical data, ensuring users have access to a holistic suite of financial information.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [fmp_company_search.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_company_search.py)             | Facilitate company search functionality on Financial Modeling Prep (FMP) based on various identifiers like ISIN, CUSIP, CIK, ticker, and company name. Offer diverse search capabilities to retrieve detailed company information, ensuring comprehensive and precise data access aligned with the parent repositorys architectural design.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [fmp_historical_data.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_historical_data.py)           | Retrieve historical stock price data, including daily and intraday data, for specified symbols and date ranges. Provide essential financial metrics and calculations, such as VWAP, to support investment analysis. Integrate efficiently with the Financial Modeling Prep API and ensure data is appropriately formatted and rounded for end-user consumption.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [fmp_quote.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_quote.py)                               | This code file is part of the `fmp_py` repository, a Python package structured for financial data analysis and manipulation. The repository encapsulates various modules focused on different aspects of financial market data. The primary purpose of the repository is to provide a comprehensive toolkit for interacting with financial market data, facilitating tasks such as fetching company information, historical data, financial statements, stock lists, and more.The critical features of the code file include:-Accessing and managing financial market data from multiple perspectives, including company information, historical data, and financial statements.-Supporting data analysis and visualization through various modules that cater to different data types and user needs.-Enabling seamless integration and usage within other projects through a well-defined API, enhancing reproducibility and consistency in financial data handling.Overall, this code file contributes significantly to the broader architecture of the `fmp_py` repository by offering specialized functionality to handle diverse financial datasets.                                                                                                                                                                                                  |
| [fmp_statement_analysis.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_statement_analysis.py)     | Src/fmp_py/fmp_financial_statements.py`The `fmp_financial_statements.py` file serves as a critical component within the `fmp_py` directory of the repository. It is responsible for handling the retrieval and processing of financial statement data, providing a structured way to access various financial reports such as income statements, balance sheets, and cash flow statements. This functionality is integral to the repository's broader goal of offering comprehensive financial data handling and analysis tools. By enabling efficient access to financial statements, this file supports advanced financial analytics and decision-making processes within the overall architecture.#### Parent Repository: `fmp-py`The `fmp-py` repository is designed to provide a Python-based interface for interacting with financial market data. It is structured to facilitate comprehensive data retrieval, processing, and analysis through robust and modular code components. This serves the end goal of allowing users to perform in-depth financial analysis leveraging various data points and insights offered by the repository. The architecture is further supported by thorough documentation, testing workflows, and a focus on community-driven enhancements as indicated by the presence of issue templates and a code of conduct. |
| [fmp_company_information.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_company_information.py)   | Summary of `fmp_company_information.py`The `fmp_company_information.py` module within the `fmp-py` repository provides functionalities for retrieving detailed company information. It serves as a crucial component of the parent architecture by enabling users to access comprehensive data about different companies, which includes general information, business summaries, and profiles. This aids in forming a holistic view of the companies being queried, thereby enhancing the repositorys capability to serve as a robust financial data retrieval and analysis tool. This module complements other files in the `src/fmp_py` directory by focusing specifically on company-centric data and integrating seamlessly with broader financial data functionalities.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [fmp_valuation.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_valuation.py)                       | The file `fmp_company_information.py` within the `fmp-py` repository is primarily responsible for retrieving and managing company-specific data, such as profiles, key metrics, and other relevant details. This functionality is crucial within the broader architecture of the `fmp-py` project, as it allows users to access and manipulate company information seamlessly. The module integrates with other components like financial statements and historical data modules, facilitating comprehensive financial analysis and research workflows.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [fmp_base.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_base.py)                                 | Serve as the foundational API client for interacting with the Financial Modeling Prep service, managing authentication and GET requests. Provide utility for type-safe data cleaning and ensure efficient handling of API sessions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [fmp_stock_list.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_stock_list.py)                     | Interact with the Financial Modeling Prep API to retrieve various stock lists and related financial data, including available indexes, exchange symbols, symbol changes, and more. The FmpStockList class aggregates these functionalities, providing seamless data access and processing for financial applications within the repositorys architecture.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [fmp_charts.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_charts.py)                             | Fmp_stock_list.py`The `fmp_stock_list.py` file is part of the `fmp-py` repository, which aims to provide a comprehensive Python package for interacting with financial market data. This specific file focuses on retrieving and managing lists of stocks, leveraging the functionalities of the parent repository to facilitate users in accessing up-to-date stock information. It integrates seamlessly with other modules in the `src/fmp_py` directory, enabling users to fetch stock lists based on various criteria, which can be crucial for tasks like portfolio management, market analysis, and financial research. The file plays an essential role in enhancing the repositorys capability to deliver diverse financial datasets to end-users efficiently.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [fmp_price_targets.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/fmp_price_targets.py)               | Provide comprehensive methods to retrieve price target data from the Financial Modeling Prep API, including consensus, summary, and detailed price targets for a given stock symbol, thereby enhancing investment decision-making capabilities within the fmp-py repositorys financial data analysis framework.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

</details>

<details closed><summary>src.fmp_py.models</summary>

| File                                                                                                                 | Summary                                                                                                                                                                                                                                                                                                                                                                      |
| ---                                                                                                                  | ---                                                                                                                                                                                                                                                                                                                                                                          |
| [price_targets.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/models/price_targets.py)             | Define data structures for representing price target consensus and summary information, facilitating organized and efficient handling of financial data within the repositorys broader architecture for financial market analysis.                                                                                                                                           |
| [statement_analysis.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/models/statement_analysis.py)   | Defines data structures essential for financial statement analysis within the parent repository. These structures encapsulate various financial scores, ratios, and key metrics, supporting comprehensive financial evaluations and data manipulation across multiple modules, enhancing the repositorys capability to offer detailed and structured financial insights.     |
| [company_information.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/models/company_information.py) | Define various data models related to company information, including stock peers, core details, market cap, executive compensation, and overall company profile, which provide structured data representations within the repositorys financial data processing architecture.                                                                                                |
| [quote.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/models/quote.py)                             | Define multiple data models central for representing various types of financial market quotes, facilitating the retrieval and manipulation of real-time and historical data related to stocks, forex, crypto, and after-market trading within the fmp-py repository architecture. These models underpin the data structure consistency and integrity across the application. |
| [upgrades_downgrades.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/models/upgrades_downgrades.py) | Defines an UpgradesDowngrades data model incorporating key attributes related to stock recommendations, such as symbol, buy/sell ratings, and consensus. Functions as a crucial component for organizing and retrieving rating data within the broader architecture of the financial market data repository.                                                                 |
| [valuation.py](https://github.com/TexasCoding/fmp-py/blob/master/src/fmp_py/models/valuation.py)                     | Define data structures for managing discounted cash flow and company rating information, essential for valuation analysis within the repositorys financial modeling capabilities. Offer comprehensive attributes for each structure, facilitating detailed and accurate financial assessments and recommendations.                                                           |

</details>

<details closed><summary>.github.workflows</summary>

| File                                                                                                       | Summary                                                                                                                                                                                                                                                                                           |
| ---                                                                                                        | ---                                                                                                                                                                                                                                                                                               |
| [test-package.yaml](https://github.com/TexasCoding/fmp-py/blob/master/.github/workflows/test-package.yaml) | Facilitate automated testing by configuring the CI/CD pipeline to run tests on the repository. Ensures the codebase remains robust and error-free by triggering test suites whenever changes are pushed, thereby maintaining code integrity and reliability throughout the development lifecycle. |

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
