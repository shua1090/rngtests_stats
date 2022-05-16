#include <stdio.h>
#include <stdlib.h>

int main(int argc, char * argv[]){
    if (argc != 2 ){
        return -1;
    }
    int count = atoi(argv[1]);

    FILE *fptr;
    fptr = fopen("/dev/urandom","rb");
    char rnums[count+1];
    fgets(rnums, count+1, fptr);
    fclose(fptr);
    // printf("%d", rnums[0]);

    return rnums[0];
}