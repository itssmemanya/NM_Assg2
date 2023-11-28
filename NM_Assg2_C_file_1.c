#include <stdio.h>
#include <float.h>
#include <math.h>

int main() 
{
    // Machine precision for C float data type
    float machine_precision = FLT_EPSILON;

    // Storing pi in a float variable
    float pi_float = (float)M_PI;

    // Storing "true" value of pi
    double pi_true = M_PI;

    // Relative error in storing pi
    double relative_error = fabs((pi_float - pi_true) / pi_true);

    printf(" Machine Precision : %e\n", machine_precision);
    printf(" Storing pi in float : %.10f\n", pi_float);
    printf(" Relative Error in Storing pi : %e\n", relative_error);

    return 0;
}

