/* Regression calculations over data-sets
 * Used to determine optimal regressions to be used
 *
*/

#include <lapacke.h>

#include "libregress.h"

// Double-variants of regression functions

// typedef struct rgr_coeff_double_struct coeff_double_t;
struct rgr_coeff_double_struct{
	double fit_coeff[3];
	double coeff_r;
};

coeff_double_t d_rgrs_irreg(double * f_arr, double * t_arr, double * arr_len, unsigned char order)
{
}

coeff_double_t d_rgrs_reg(double * f_arr, double interval, double * arr_len, unsigned char order)
{
}

coeff_double_t d_rgrs_inv(double * f_arr, double * arr_len, unsigned char order)
{
	return d_rgrs_reg(f_arr, 1.0, arr_len, order);
}

// Float-variants of regression functions

struct rgr_coeff_float_struct{
	float fit_coeff[3];
	float coeff_r;
};

coeff_float_t f_rgrs_irreg(float * f_arr, float * t_arr, float * arr_len, unsigned char order)
{
}

coeff_float_t f_rgrs_reg(float * f_arr, float interval, float * arr_len, unsigned char order)
{
}

coeff_float_t f_rgrs_inv(float * f_arr, float * arr_len, unsigned char order)
{
	return f_rgrs_reg(f_arr, 1.0f, arr_len, order);
}
