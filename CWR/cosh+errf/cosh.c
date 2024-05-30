#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#define PI 3.14159265358979323846

double integrand(double x);
double cosh_midpoint(double x, double delta_x);
double cosh_simpson(double x, double delta_x);


int main()
{

	FILE* myFile = fopen("cosh.txt", "w");
	int N = 7;
	double x = 1;
	double delta_x = 1e-1;
	for(int j = 0; j < N; j++)
	{
			fprintf(myFile, "%.15lf \t %.15lf \t %.15lf \n", delta_x, cosh_simpson(x, delta_x), cosh_midpoint(x, delta_x));
			delta_x = 1.0/(j+1);
	}
	fclose(myFile);
	
}


double cosh_midpoint(double x, double delta_x)
{
	int N = x / delta_x;
	double result = 0;
	double m = 0;
	for(int i = 1; i <= N; i++){
		m = (i * delta_x + (i + 1) * delta_x) / 2;
		result += integrand(m);
	}
	result *= delta_x;
	return result;
}


double cosh_simpson(double x, double delta_x)
{
	int sign = 1;
	if(x < 0) sign = -1;
	int N = sign * x / delta_x;
	double result = 0;
	double m = 0;
	for(int i = 1; i <= N; i++){
		m = (i * delta_x + (i + 1) * delta_x) / 2;
		result += integrand(i * delta_x) + 4 * integrand(m) + integrand((i + 1) * delta_x);
	}
	result *= delta_x/6 * sign;
	return result;
}


double integrand(double x)
{
	double result = cosh(x);
	return result;
}
