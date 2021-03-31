#pragma once
#include <cstdarg>
namespace Eloquent {
    namespace ML {
        namespace Port {
            class SVM {
                public:
                    /**
                    * Predict class for features vector
                    */
                    int predict(float *x) {
                        float kernels[40] = { 0 };
                        float decisions[3] = { 0 };
                        int votes[3] = { 0 };
                        kernels[0] = compute_kernel(x,   5.1  , 3.3  , 1.7  , 0.5 );
                        kernels[1] = compute_kernel(x,   4.8  , 3.1  , 1.6  , 0.2 );
                        kernels[2] = compute_kernel(x,   4.8  , 3.4  , 1.9  , 0.2 );
                        kernels[3] = compute_kernel(x,   5.1  , 3.8  , 1.9  , 0.4 );
                        kernels[4] = compute_kernel(x,   5.1  , 2.5  , 3.0  , 1.1 );
                        kernels[5] = compute_kernel(x,   4.9  , 2.4  , 3.3  , 1.0 );
                        kernels[6] = compute_kernel(x,   6.1  , 3.0  , 4.6  , 1.4 );
                        kernels[7] = compute_kernel(x,   6.4  , 3.2  , 4.5  , 1.5 );
                        kernels[8] = compute_kernel(x,   5.4  , 3.0  , 4.5  , 1.5 );
                        kernels[9] = compute_kernel(x,   6.0  , 2.9  , 4.5  , 1.5 );
                        kernels[10] = compute_kernel(x,   6.0  , 3.4  , 4.5  , 1.6 );
                        kernels[11] = compute_kernel(x,   6.6  , 2.9  , 4.6  , 1.3 );
                        kernels[12] = compute_kernel(x,   6.5  , 2.8  , 4.6  , 1.5 );
                        kernels[13] = compute_kernel(x,   5.7  , 2.6  , 3.5  , 1.0 );
                        kernels[14] = compute_kernel(x,   6.3  , 3.3  , 4.7  , 1.6 );
                        kernels[15] = compute_kernel(x,   6.9  , 3.1  , 4.9  , 1.5 );
                        kernels[16] = compute_kernel(x,   6.1  , 2.8  , 4.7  , 1.2 );
                        kernels[17] = compute_kernel(x,   6.8  , 2.8  , 4.8  , 1.4 );
                        kernels[18] = compute_kernel(x,   6.3  , 2.5  , 4.9  , 1.5 );
                        kernels[19] = compute_kernel(x,   6.0  , 2.7  , 5.1  , 1.6 );
                        kernels[20] = compute_kernel(x,   6.3  , 2.3  , 4.4  , 1.3 );
                        kernels[21] = compute_kernel(x,   6.1  , 2.9  , 4.7  , 1.4 );
                        kernels[22] = compute_kernel(x,   5.9  , 3.2  , 4.8  , 1.8 );
                        kernels[23] = compute_kernel(x,   5.8  , 2.7  , 5.1  , 1.9 );
                        kernels[24] = compute_kernel(x,   5.8  , 2.7  , 5.1  , 1.9 );
                        kernels[25] = compute_kernel(x,   6.0  , 3.0  , 4.8  , 1.8 );
                        kernels[26] = compute_kernel(x,   6.2  , 2.8  , 4.8  , 1.8 );
                        kernels[27] = compute_kernel(x,   5.7  , 2.5  , 5.0  , 2.0 );
                        kernels[28] = compute_kernel(x,   6.0  , 2.2  , 5.0  , 1.5 );
                        kernels[29] = compute_kernel(x,   4.9  , 2.5  , 4.5  , 1.7 );
                        kernels[30] = compute_kernel(x,   6.3  , 2.9  , 5.6  , 1.8 );
                        kernels[31] = compute_kernel(x,   6.9  , 3.1  , 5.4  , 2.1 );
                        kernels[32] = compute_kernel(x,   6.3  , 2.8  , 5.1  , 1.5 );
                        kernels[33] = compute_kernel(x,   5.9  , 3.0  , 5.1  , 1.8 );
                        kernels[34] = compute_kernel(x,   5.6  , 2.8  , 4.9  , 2.0 );
                        kernels[35] = compute_kernel(x,   6.4  , 2.7  , 5.3  , 1.9 );
                        kernels[36] = compute_kernel(x,   6.9  , 3.1  , 5.1  , 2.3 );
                        kernels[37] = compute_kernel(x,   6.5  , 3.2  , 5.1  , 2.0 );
                        kernels[38] = compute_kernel(x,   6.7  , 3.0  , 5.2  , 2.3 );
                        kernels[39] = compute_kernel(x,   6.4  , 3.1  , 5.5  , 1.8 );
                        decisions[0] = 0.041571413157
                        + kernels[0] * 100.0
                        + kernels[1] * 24.132793286987
                        + kernels[2] * 100.0
                        + kernels[3] * 32.189967031599
                        + kernels[4] * -100.0
                        + kernels[5] * -100.0
                        + kernels[13] * -56.322760318586
                        ;
                        decisions[1] = 0.026876688004
                        + kernels[0] * 22.006220839835
                        + kernels[2] * 77.993779160165
                        + kernels[29] * -100.0
                        ;
                        decisions[2] = -0.269178726646
                        + kernels[6] * 100.0
                        + kernels[7] * 100.0
                        + kernels[8] * 100.0
                        + kernels[9] * 100.0
                        + kernels[10] * 100.0
                        + kernels[11] * 94.530815601748
                        + kernels[12] * 100.0
                        + kernels[14] * 100.0
                        + kernels[15] * 100.0
                        + kernels[16] * 100.0
                        + kernels[17] * 100.0
                        + kernels[18] * 100.0
                        + kernels[19] * 100.0
                        + kernels[20] * 100.0
                        + kernels[21] * 100.0
                        + kernels[22] * 100.0
                        + kernels[23] * -100.0
                        + kernels[24] * -100.0
                        + kernels[25] * -100.0
                        + kernels[26] * -100.0
                        + kernels[27] * -100.0
                        + kernels[28] * -100.0
                        + kernels[29] * -100.0
                        + kernels[30] * -2.643147873176
                        + kernels[31] * -100.0
                        + kernels[32] * -100.0
                        + kernels[33] * -100.0
                        + kernels[34] * -100.0
                        + kernels[35] * -100.0
                        + kernels[36] * -100.0
                        + kernels[37] * -100.0
                        + kernels[38] * -91.887667728571
                        + kernels[39] * -100.0
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

                        return exp(-0.001 * kernel);
                    }
                };
            }
        }
    }
