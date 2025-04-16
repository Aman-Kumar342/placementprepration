#include <stdio.h>
#include <string.h>

#define SUCCESS 1
#define FAILED 0

int E(), Edash(), T(), Tdash(), F();
const char *pt;
char grammar[64];

int main() {
    strcpy(grammar, "i+(i+i)*i");
    pt = grammar;

    puts("Input Action");

    if (E() && *pt == '\0') {
        puts("String is successfully parsed");
        return 0;
    } else {
        puts("Error in parsing String");
        return 1;
    }
}

int E() {
    printf("%-16s E -> T E'\n", pt);
    if (T()) {
        if (Edash())
            return SUCCESS;
    }
    return FAILED;
}

int Edash() {
    if (*pt == '+') {
        printf("%-16s E' -> + T E'\n", pt);
        pt++;
        if (T()) {
            if (Edash())
                return SUCCESS;
        }
        return FAILED;
    }

    printf("%-16s E' -> $\n", pt);
    return SUCCESS;
}

int T() {
    printf("%-16s T -> F T'\n", pt);
    if (F()) {
        if (Tdash())
            return SUCCESS;
    }
    return FAILED;
}

int Tdash() {
    if (*pt == '*') {
        printf("%-16s T' -> * F T'\n", pt);
        pt++;
        if (F()) {
            if (Tdash())
                return SUCCESS;
        }
        return FAILED;
    }

    printf("%-16s T' -> $\n", pt);
    return SUCCESS;
}

int F() {
    if (*pt == '(') {
        printf("%-16s F -> (E)\n", pt);
        pt++;
        if (E()) {
            if (*pt == ')') {
                pt++;
                return SUCCESS;
            }
            return FAILED;
        }
        return FAILED;
    } else if (*pt == 'i') {
        printf("%-16s F -> i\n", pt);
        pt++;
        return SUCCESS;
    }
    return FAILED;
}
