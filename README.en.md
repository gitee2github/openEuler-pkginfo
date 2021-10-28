# openEuler-pkginfo

#### Introduction
openEuler-pkginfo is a collection of query tools for easily maintaining openEuler.

#### Description
openEuler-pkginfo encapsulates APIs provided by Gitee to simplify statistics collection, information query, automatic MR submission, and more.

#### Objectives

1. Statistics collection commands, including those for collecting statistics on user code contributions.
2. Information query commands, including those for searching for issues by keyword and querying issue/MR details.
3. Automatic submission commands, including those for automatically creating MRs and creating/updating issues.

Mentor: overweight
Contact: hexiaowen@huawei.com

#### Milestones

- 2020.07.30 release v0.1: supports statistics functions.
- 2020.08.30 release v0.2: supports information query functions.
- 2020.09.30 release v1.0: supports submission functions.

**TODO**

(release v0.1)
- Use Python to connect to the API pages provided by Gitee to obtain data.  √
- Organization information statistics: Display the number of repositories and repository links.  √
- Repository information statistics: Display information such as the number of branches and latest released versions.
- Individual contribution statistics: Display a user's contribution to a repository (including the amount of submitted code and the number of issues).

(release v0.2)
- Repository information query: Search for the detailed information about an MR/commit/issue in the repository based on the submitter/change file.
- Issue query: Search for an issue by keyword.

(release v1.0)
- Submit an MR: create the MR, update the MR, and assign the reviewer.
- Submit an issue: Create and update an issue.
- Submit and pull code: Automatically submit and pull code.

#### Gitee Features

1.  Use Readme_XXX.md to mark README files with different languages, such as Readme_en.md and Readme_zh.md.
2.  Gitee blog: [blog.gitee.com](https://blog.gitee.com)
3.  You can visit [https://gitee.com/explore](https://gitee.com/explore) to learn about excellent open source projects on Gitee.
4.  [GVP](https://gitee.com/gvp) is short for Gitee Most Valuable Project.
5.  User manual provided by Gitee: [https://gitee.com/help](https://gitee.com/help)
6.  Gitee Cover People is a column to display Gitee members' demeanor. Visit [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/).
