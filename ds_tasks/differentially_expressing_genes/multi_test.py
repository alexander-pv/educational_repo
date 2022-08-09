import scipy
from scipy import stats
import time
import numpy as np
import pandas as pd
import multiprocessing as mp


def timeit(f):
    def timed(*args, **kw):
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()
        print('ETA: %2.4f sec' % (te-ts))
        return result
    return timed


def permutation_t_stat_ind(sample1, sample2):
    return np.mean(sample1) - np.mean(sample2)


def get_random_combinations(n1, n2, max_combinations):
    index = [i for i in range(n1 + n2)]
    indices = set([tuple(index)])
    for i in range(max_combinations - 1):
        np.random.shuffle(index)
        indices.add(tuple(index))
    return [(index[:n1], index[n1:]) for index in indices]


def permutation_zero_dist_ind(sample1, sample2, max_combinations = None):
    joined_sample = np.hstack((sample1, sample2))
    n1 = len(sample1)
    n = len(joined_sample)
    
    if max_combinations:
        indices = get_random_combinations(n1, len(sample2), max_combinations)
    else:
        indices = [(list(index), filter(lambda i: i not in index, range(n))) \
                    for index in itertools.combinations(range(n), n1)]
    
    distr = [joined_sample[list(i[0])].mean() - joined_sample[list(i[1])].mean() \
             for i in indices]
    return distr


def permutation_test(sample, mean, max_permutations = None, alternative = 'two-sided'):
    if alternative not in ('two-sided', 'less', 'greater'):
        raise ValueError("alternative not recognized\n"
                         "should be 'two-sided', 'less' or 'greater'")
    
    t_stat = permutation_t_stat_ind(sample, mean)
    
    zero_distr = permutation_zero_dist_ind(sample, mean, max_permutations)
    
    if alternative == 'two-sided':
        return sum([1. if abs(x) >= abs(t_stat) else 0. for x in zero_distr]) / len(zero_distr)
    
    if alternative == 'less':
        return sum([1. if x <= t_stat else 0. for x in zero_distr]) / len(zero_distr)

    if alternative == 'greater':
        return sum([1. if x >= t_stat else 0. for x in zero_distr]) / len(zero_distr)

@timeit
def parallelize_dataframe_compute(function, data_chunks):
    """
    Параллелизация расчетов с pandas.
    :param function: python function
    :param data_chunks: pd.DataFrame slices
    :return: pd.DataFrame
    """
    pool = mp.Pool(mp.cpu_count()//4)
    results = pool.map(function, data_chunks)
    pool.close()
    pool.join()
    df_final = pd.concat(results)
    return df_final


def make_tests(args):
    """
    Выполняем тесты Стьюдента (Уэлча) и перестановочный тест
    :param args:
    :return:
    """
    df_chunk, gene_name = args
    dict_hypothesis = {'Gene': [], 
                       'n_en_student_p_value': [],
                       'en_c_student_p_value': [],

                       'n_en_permutation_p_value': [],
                       'en_c_permutation_p_value': [],
                      }  
    dict_hypothesis['Gene'].append(gene_name)

    # Student (Welch)
    dict_hypothesis['n_en_student_p_value'].append(
        stats.ttest_ind(df_chunk[df_chunk['Diagnosis'] == 'normal'][gene_name],
                        df_chunk[df_chunk['Diagnosis'] == 'early neoplasia'][gene_name], equal_var=False)[1])
    dict_hypothesis['en_c_student_p_value'].append(
        stats.ttest_ind(df_chunk[df_chunk['Diagnosis'] == 'early neoplasia'][gene_name],
                        df_chunk[df_chunk['Diagnosis'] == 'cancer'][gene_name], equal_var=False)[1])

    # Permutational criteria
    dict_hypothesis['n_en_permutation_p_value'].append(
        permutation_test(df_chunk[df_chunk['Diagnosis'] == 'normal'][gene_name].values.tolist(),
                         df_chunk[df_chunk['Diagnosis'] == 'early neoplasia'][gene_name].values.tolist(),
                         max_permutations=10000))
    dict_hypothesis['en_c_permutation_p_value'].append(
        permutation_test(df_chunk[df_chunk['Diagnosis'] == 'early neoplasia'][gene_name].values.tolist(),
                         df_chunk[df_chunk['Diagnosis'] == 'cancer'][gene_name].values.tolist(),
                         max_permutations=10000))
    df_tests = pd.DataFrame(dict_hypothesis)
    return df_tests
