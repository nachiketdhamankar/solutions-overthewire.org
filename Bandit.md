# Bandit
<strong>Level 0</strong>

ssh bandit0@bandit.labs.overthewire.org

password bandit0


<strong>Level 1 -> Level 2</strong>

cat readme

O/P : boJ9jbbUNNfktd78OOpsqOltutMc3MY1


ssh bandit1@bandit.labs.overthewire.org

password boJ9jbbUNNfktd78OOpsqOltutMc3MY1


cat ./-

O/P : CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9


ssh bandit2@bandit.labs.overthewire.org

password : CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9


<strong>Level 2 -> Level 3</strong>


cat spaces\ in\ this\ filename

O/P : UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK


ssh bandit3@bandit.labs.overthewire.org

password : UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK


<strong>Level 3 -> Level 4</strong>

cd inhere

ls -a # -a is used to show all files including . and ..

cat .hidden

O/P : pIwrPrtPN36QITSp3EQaw936yaFoFgAB


ssh bandit4@bandit.labs.overthewire.org

password : pIwrPrtPN36QITSp3EQaw936yaFoFgAB


<strong>Level 4 -> Level 5</strong>

cd inhere

ls

for file in *; do echo $file; cat ./$file; done

cat ./-file07

O/P : koReBOKuIDDepwhWk7jZC0RTdopnAYKh



Alternative method :- (Trial and error) Find the number of files by a ls -a command and then keep on trying each file with file -f command.

Ex. : file -f -file00 and so on



ssh bandit5@bandit.labs.overthewire.org

password : koReBOKuIDDepwhWk7jZC0RTdopnAYKh
