#ifndef LIB_REGRESS_H
#define LIB_REGRESS_H

typedef struct rgr_coeff_double_struct coeff_double_t;
typedef struct rgr_coeff_float_struct coeff_float_t;

extern coeff_double_t d_rgrs_irreg(double * f_arr, double * t_arr, double * arr_len, unsigned char order);

extern coeff_double_t d_rgrs_reg(double * f_arr, double interval, double * arr_len, unsigned char order);
extern coeff_double_t d_rgrs_inv(double * f_arr, double * arr_len, unsigned char order);
extern coeff_float_t f_rgrs_irreg(float * f_arr, float * t_arr, float * arr_len, unsigned char order);

extern coeff_float_t f_rgrs_reg(float * f_arr, float interval, float * arr_len, unsigned char order);
extern coeff_float_t f_rgrs_inv(float * f_arr, float * arr_len, unsigned char order);

#endif
