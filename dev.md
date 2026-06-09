# Development Workflow

There will be a few steps in the development workflow. I will split it up into 3 sections:
-   Setup
-   Commiting
-   Finalizing

This will enable us to develop cleanly and without much overlap. Let's start with the setup.

**Note**
If you haven't done so already, make sure you have the following installed:
-   A Coding Editor
-   The `git` CLI
-   Docker (I prefer the CLI)
-   ...Add any missing dependencies

## Setup

When we have a problem we want to solve in our application, whether it be a new feature, a bug or any `issue` we would like to fix, we should start by doing just that. Navigate to the repo in our GitHub and click on the `Issues` Tab. **Before creating your own issue** make sure that one for it doesn't already exist. If it doesn't makean issue, give it a title and a description. Feel free to add any details you feel are necessary in the description.

Great! now we have an issue to solve. What we now want to do is make sure we are not solving the issue in the `main` branch. The easiest way to do this is to navigate to the specific issue page we want to solve and click on the link that says `Create a branch for this issue or link a pull request`. Follow the instructions to create a branch. This branch is useful because it gives us a copy of the main code without affecting it while we develop.Now we will be able to submit changes to this branch while we develop without affecting the final code. Once we are ready to put it into our `main` branch, we can create what is called a `pull request` and `merge` it into the main branch. We will handle how to do that in the `Finalizing` stage.

Now that we have create the branch, we need to get it onto our computer. To do this we will use the `git` CLI. Open a terminal and navigate in it to the directory you would like the project to appear. Copy the link of the repo and use the following command:
```
git clone <PUT URL HERE>
```
This may ask for authentication so put your password in. You should see it downloading the repo. Once it is done we should see a folder with the name of our project in it. Navigate into that folder. Try typing
```
git status
```
This command gives us the current state of our local repository. To change to the branch we just created we use:
```
git checkout <BRANCH-NAME>
```
This changes the version of the files we have to match the branch we want. Now we can edit/add/delete files. 

# Development
Try editing/adding now, either make a file or edit an existing one. Make sure to save. Once you saved repeat the command we did earlier:
```
git status
```
You should now see some **red** changes that correspond to the files you added or changed. In git what we do is **commit** changes to our branch when we want to. To do that, we first have to **add** them to the repo. The command to do that is:
```
git add <FILE_PATH>
```
Now if we do `git status` we should see the files we added in **green**. Great! We are now ready to commit them to our branch. To commit them we use the command:
```
git commit -m "PUT YOUR COMMIT MESSAGE IN THESE QUOTES"
```
This makes a **commit** that contains the changes we added. This helps upload code in small segments rather than making massive changes that are hard to track. These changes are now available in our **local** branch but if we were to check the branch in GitHub we would see no changes. To **push** the changes up to the branch on GitHubwe use the command
```
git push
```
This uploads whatever changes we have locally to the remote branch so that others can **pull** the changes.
Awesome! This is the process to develop and we can keep repeating it whenever we make changes. We do this over and over and over until we are done with the **issue**. That is the development process!
# Finalizing
To finalize the changes and put them into the `main` branch, we can navigate to the branch we have been working on. It should popup and ask if you want to make a `pull request`, click whatever makes it create one because that is what we want to do. Most of the defaults should be good but make sure to link the issue by adding a description with something like `Closes #<issue_id>`. This should notify GitHub that this change closes the issue we've been working on. Make sure you have the correct amount of approvals and we can just click `Merge`. Voila! We merged it into main.
