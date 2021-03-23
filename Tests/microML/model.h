#pragma once
#include <cstdarg>
#include <stdint.h>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
namespace Eloquent {
    namespace ML {
        namespace Port {
            class SVM {
                public:
                    /**
                    * Predict class for features vector
                    */
                    int predict(float *x) {
                        float kernels[22] = { 0 };
                        float decisions[3] = { 0 };
                        int votes[3] = { 0 };
                        kernels[0] = compute_kernel(x,   5.1  , 3.3  , 1.7  , 0.5 );
                        kernels[1] = compute_kernel(x,   4.8  , 3.4  , 1.9  , 0.2 );
                        kernels[2] = compute_kernel(x,   5.7  , 4.4  , 1.5  , 0.4 );
                        kernels[3] = compute_kernel(x,   4.4  , 2.9  , 1.4  , 0.2 );
                        kernels[4] = compute_kernel(x,   5.1  , 2.5  , 3.0  , 1.1 );
                        kernels[5] = compute_kernel(x,   5.4  , 3.0  , 4.5  , 1.5 );
                        kernels[6] = compute_kernel(x,   6.0  , 2.9  , 4.5  , 1.5 );
                        kernels[7] = compute_kernel(x,   6.9  , 3.1  , 4.9  , 1.5 );
                        kernels[8] = compute_kernel(x,   6.3  , 2.5  , 4.9  , 1.5 );
                        kernels[9] = compute_kernel(x,   6.0  , 2.7  , 5.1  , 1.6 );
                        kernels[10] = compute_kernel(x,   5.0  , 2.0  , 3.5  , 1.0 );
                        kernels[11] = compute_kernel(x,   6.1  , 2.9  , 4.7  , 1.4 );
                        kernels[12] = compute_kernel(x,   5.9  , 3.2  , 4.8  , 1.8 );
                        kernels[13] = compute_kernel(x,   7.7  , 2.6  , 6.9  , 2.3 );
                        kernels[14] = compute_kernel(x,   6.0  , 3.0  , 4.8  , 1.8 );
                        kernels[15] = compute_kernel(x,   6.2  , 2.8  , 4.8  , 1.8 );
                        kernels[16] = compute_kernel(x,   6.0  , 2.2  , 5.0  , 1.5 );
                        kernels[17] = compute_kernel(x,   4.9  , 2.5  , 4.5  , 1.7 );
                        kernels[18] = compute_kernel(x,   6.3  , 2.8  , 5.1  , 1.5 );
                        kernels[19] = compute_kernel(x,   5.9  , 3.0  , 5.1  , 1.8 );
                        kernels[20] = compute_kernel(x,   7.9  , 3.8  , 6.4  , 2.0 );
                        kernels[21] = compute_kernel(x,   6.5  , 3.2  , 5.1  , 2.0 );
                        decisions[0] = 0.010039968425
                        + kernels[0] * 3.745196541043
                        + kernels[1] * 0.500353175187
                        + kernels[4] * -4.24554971623
                        ;
                        decisions[1] = -0.218900273614
                        + kernels[0] * 0.210104061139
                        + kernels[1] * 0.809249938639
                        + kernels[2] * 0.450011453533
                        + kernels[3] * 0.331819700228
                        + kernels[13] * -0.170503129399
                        + kernels[17] * -1.219885724575
                        + kernels[20] * -0.410796299565
                        ;
                        decisions[2] = -0.648851391098
                        + kernels[5] * 10.0
                        + kernels[6] * 9.125786921452
                        + kernels[7] * 9.212549048903
                        + kernels[8] * 10.0
                        + kernels[9] * 10.0
                        + kernels[10] * 0.032707167234
                        + kernels[11] * 10.0
                        + kernels[12] * 10.0
                        + kernels[14] * -10.0
                        + kernels[15] * -10.0
                        + kernels[16] * -10.0
                        + kernels[17] * -8.371043137589
                        + kernels[18] * -10.0
                        + kernels[19] * -10.0
                        + kernels[21] * -10.0
                        ;
                        votes[decisions[0] > 0 ? 0 : 1] += 1;
                        votes[decisions[1] > 0 ? 0 : 2] += 1;
                        votes[decisions[2] > 0 ? 1 : 2] += 1;
                        int val = votes[0];
                        int idx = 0;

                        for (int i = 1; i < 3; i++) {
                            if (votes[i] > val) {
                                val = votes[i];
                                idx = i;
                            }
                        }

                        return idx;
                    }

                protected:
                    /**
                    * Compute kernel between feature vector and support vector.
                    * Kernel type: rbf
                    */
                    float compute_kernel(float *x, ...) {
                        va_list w;
                        va_start(w, 4);
                        float kernel = 0.0;

                        for (uint16_t i = 0; i < 4; i++) {
                            kernel += pow(x[i] - va_arg(w, double), 2);
                        }

                        return exp(-0.1 * kernel);
                    }
                };
            }
        }
    }