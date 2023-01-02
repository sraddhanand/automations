from git import Repo
import re

vs_version = "v1.2.0"
file_to_change = "fastapi/values.yaml"
checkout_to_path = "local/directory/to/clone/the/repo"
clone_repo_url = "https://github.com/sraddhanand/helm_charts.git"

def git_checkout(repo, branch_name):
    new_branch = repo.create_head(branch_name)
    repo.head.reference = new_branch
    return repo, new_branch

# update file
def replace_version(file_name, version):
    print(file_name)
    with open(file_name, 'r') as file:
        data = file.read()
    data = re.sub(r'tag: "v1"', r"tag: " + str(version), data)
    # Write data back 
    with open(file_name, 'w') as file:
        file.write(data)

repo = Repo.clone_from(url=clone_repo_url, to_path=checkout_to_path)
repo, new_branch = git_checkout(repo, "test")
replace_version("helm_charts/" + file_to_change, vs_version)
# commit
index = repo.index
index.add([file_to_change])
index.commit(message="set tag to " + vs_version)
# push the branch
repo.remotes.origin.push(refspec=new_branch)

