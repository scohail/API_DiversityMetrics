<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/scohail/API_DeversityComputation">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">API_DeversityComputation</h3>

  <p align="center">
    This project aims to provide a simple and easy to use API for diversity computation in a given dataset. 
    <br />
    <a href="https://github.com/scohail/API_DiversityComputation"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/scohail/API_DiversityComputation">View Demo</a>
    ·
    <a href="https://github.com/scohail/API_DiversityComputation/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/scohail/API_DiversityComputation/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)


This is a academic project that aims to implement a UI and API for diversity computation for machine learninng models in a given dataset. The project is divided into two parts: the API and the UI. The API is responsible for computing the diversity of a given dataset, while the UI is responsible for providing a user-friendly interface for the user to interact with the API. The API is implemented using Python. The UI is not implemented yet, but it will be implemented soon.

There are many ways to compute diversity in both types of ML models `Regression` and `Classification`. The Decirsity metrics implemented in this project are:
* `Regression Pairwise Diversity`:
  * `CorrelationCoefficient` : Calculate the Pearson correlation coefficient between the outputs of two regressors.
  * `MeanSquaredDifference` : Calculate the mean squared difference between the outputs of two regressors.
  * `MeanAbsoluteDifference` : Calculate the mean absolute difference between the outputs of two regressors.
  * `ErrorCorrelation` : Calculate the error correlation between the outputs of two regressors.
  * `Disagreement` : Calculate the disagreement between the outputs of two regressors.
  * `RankCorrelation` : Calculate the rank correlation between the outputs of two regressors.
  * `QStatistics` : Calculate the Q statistics between the outputs of two regressors.
  * `CovarianceError` : Calculate the covariance error between the outputs of two regressors.
  * `PartialCorrelation` : Calculate the partial correlation between the outputs of two regressors. 
  * `DoubleFault` : Calculate the double fault between the outputs of two regressors.

* `Regression Nonpairwise diversity` :
  * `Variance Outputs`:Calculate the Variance of Outputs metric for an ensemble of regressors.
  * `Ambiguity`:Calculate the expected disagreement between base learners and the ensemble prediction.the Ambiguity metric for an ensemble of regressors.
  * `Variance Coefficients`:Calculate The ratio of the standard deviation to the mean of the outputs for each data point, highlighting relative variability.
  * `Diversity density`:Estimate the density of predictions in the output space and assess diversity inversely proportional to this density.Calculate
  * `Error variance`: Calculate the Variance of the errors across all base regressors, reflecting diversity in model errors.
  * `Ambiguity decomposition`: calculate the variance of the errors across all base regressors, reflecting diversity in model errors.

* `Classification Pairwise Diversity`:
  * `Correlation Coefficient`: Correlation Coefficient (ρ) metric to measure the similarity between two classifiers based on their predictions and true labels.
  * `Qstatistics`: Q Statistics metric to measure the level of agreement between two classifiers.
  * `Difference measure`: Differences Measure metric that captures the proportion of examples where the two classifiers disagree.
  * `Dauble Fault`: Double Fault Measure metric that considers the failure of two classifiers simultaneously
  * `Combination of Diversity Measures and Double Fault`: This measure is a combination between the Differences Measure and the Double Fault Measure 

* `Classification Nonpairwise Diversity`:
  * `Entropy`: Calculate the entropy of the ensemble predictions for a classification task.
  * `Kohavi Wolpert Variance`: measure the diversity of a compound set for binary classifiers.
  * `Measurement interrater agreement`: Calculate the the agreement level inside the classifiers set


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![python][python.org]][python-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- §§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§ -->


<!-- §§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§ -->









<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://legacy.python.org/community/logos/python-logo.png
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
[python.org]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[python-url]: https://www.python.org/
