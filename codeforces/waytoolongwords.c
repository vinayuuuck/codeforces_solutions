#include <stdio.h>

int main(){
    int i;
    
    scanf("%d", &i);

    // loop for i times
    for(int j = 0; j < i; j++){
        // get the word
        char word[100];
        scanf("%s", word);

        // get the length of the word
        int length = 0;
        while(word[length] != '\0'){
            length++;
        }

        // if the length is greater than 10, print the first and last letter
        if(length > 10){
            printf("%c%d%c\n", word[0], length - 2, word[length - 1]);
        } else {
            printf("%s\n", word);
        }
    }
}