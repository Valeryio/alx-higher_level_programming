#include <stdio.h>
#include <stdlib.h>
#include <wchar.h>

int main(int argc, char* argv)
{
	int **ptop = NULL, *p = NULL, *s = NULL, i = 1;
	int addr = 0;
	long int u = 0;
	wchar_t dest[20];


	p = malloc(sizeof(int) * 4);
	s = &i;
	ptop = &p;

	//u = *ptop;

	wcscpy(dest, *ptop);

	wprintf(L"Source : %ls\n", dest);
	printf("VOici l'adresse de p : %ls and %ls\n", *ptop, dest);
	if (!p)
	{
		free(p);
		return (0);
	}
	p[0] = 100;
	addr = 4;

	if (s != p)
		printf("OUi les adresses son diferentes\n");
	
	printf("VOici l'adresse de p : %p\n", &p);
	printf("Pour commencer, voici l'adresse de P : %d\n", addr);
	printf("VOici donc p[0] : %d et son adresse : %p\n", p[0], &p[0]);
	
	return (0);
}
