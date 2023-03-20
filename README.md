GIT-PROJECT.

ABOUT: This is sample git project which is intended to Push a sample local file to GitHub repository.

TOOLS USED: AWS EC2, Git, Python file and GitHub.

Process: to do this project first we need to go to EC2 console-> login , go to launch instance and Launch a instance by naming it.
        
![Screenshot (7)](https://user-images.githubusercontent.com/114085306/226391214-d578fcc8-4104-4769-9998-7cbe90e89420.png)
  
* After launching that instance,go take IP Publi address and we can open GitBash and we can ssh into it. EX ssh -i ~/Downloads/(pemkey) ec2-user@123.45.67.120.
![Screenshot (8)](https://user-images.githubusercontent.com/114085306/226392148-c4cdb673-00b7-42e4-90a7-eb2887d3703d.png)

We can see the Terminal like above if we did it correct. 

Then we need to go to Github and create a repository to push our code in to it. For that we can visit our GitHub account and create a Repository it fallows fallowing steps.
          1. click on New repository.
          2.Give repository a name.
          3.select READme. file so that we can document our work in it.
          4.If you want ot public select public or can keep it Private.
          5.Then click on create repository. and it gets created.

Next create a Directory using mkdir <dirname> and change directory into it using cd<dir name>
        
![Screenshot (9)](https://user-images.githubusercontent.com/114085306/226394343-980848d6-d266-4d29-a489-a6505b374975.png)
 Then give global configurations for that repository to do commits (If u dont give global user configurations it won't allow you to push the code.)
 the global configurations are as fallows:
          *git config --global user.name"PradeepBollepalli"
          *git config --global user.email"<email address>"
        
        
