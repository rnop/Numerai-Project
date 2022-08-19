def load_numerai_data(DATA_PATH, overlap_eras=False, n_subsample=4, remove_bad_features=True):
    '''
    Returns a loaded and pre-processed Pandas DataFrame.
    Recommended to use the int8.parquet files!

        overlap_eras: Keep data from overlapping eras with the risk of data leakage (default=False)
        n_subsample: Subsamples observations by the nth eras if overlap_eras=False (default=4)
        remove_bad_features: Remove features Numerai officially declared "dangerous" (as of Aug 3rd, 2022)

    Get a list of all datasets using `NumerAPI().list_datasets()`.
    Download the data using NumerAPI().download_dataset(NUMERAI_DATA_PATH, DATA_PATH)
    '''
    df = pd.read_parquet(DATA_PATH)
    df['erano'] = df.era.astype(np.int8)
    if overlap_eras == False:
      nonoverlap_eras = np.arange(df['erano'][0], df['erano'][-1], n_subsample) 
      df = df[df['erano'].isin(nonoverlap_eras)]

    if remove_bad_features == True:
      bad_features = ['feature_palpebral_univalve_pennoncel',
                      'feature_unsustaining_chewier_adnoun',
                      'feature_brainish_nonabsorbent_assurance',
                      'feature_coastal_edible_whang',
                      'feature_disprovable_topmost_burrower',
                      'feature_trisomic_hagiographic_fragrance',
                      'feature_queenliest_childing_ritual',
                      'feature_censorial_leachier_rickshaw',
                      'feature_daylong_ecumenic_lucina',
                      'feature_steric_coxcombic_relinquishment']
      df = df.drop(bad_features, axis=1)

    return df

def compute_feature_target_corr_by_era(df, features, target='target', era_col='erano'):
    '''
    Returns a Pandas DataFrame containing each individual feature-target correlation by eras.
    Useful to see how correlations change over time for each feature. 
    '''
    feature_target_corr_df = pd.DataFrame(index=features).sort_index()
    for era in set(df[era_col]):
      feature_scores = {feature: score for feature, score in zip(features, np.corrcoef(df[df.erano==era][[target]+features].T)[1:,0])}
      feature_target_corr_df[f'era_{era}'] = pd.Series(feature_scores).sort_values()
    return feature_target_corr_df

def correlation_score(y_true, y_pred):
    '''
    Computes the Pearson Correlation of the model's predictions to the actual targets.
    '''
    return np.corrcoef(y_true, y_pred)[0,1]

def score(df):
    '''
    Takes in Pandas DataFrame and calculates Spearman's Correlation using the prediction column.
    '''
    # method="first" breaks ties based on order in array
    return np.corrcoef(
          df['target'],
          df['prediction'].rank(pct=True, method="first")
      )[0,1]

def run_analytics(era_scores):
    '''
    Computes and visualizes the mean correlation and standard deviation of the model's predictions across eras.
    Also computes and visualizes the overall Sharpe Ratio and Hit Rate (profitable eras). 
    '''
    print(f"Mean Correlation: {era_scores.mean():.4f}")
    print(f"Standard Deviation: {era_scores.std():.4f}")
    print(f"Mean Pseudo-Sharpe: {era_scores.mean()/era_scores.std():.4f}")
    print(f'Hit Rate (% positive eras): {era_scores.apply(lambda x: np.sign(x)).value_counts()[1]/len(era_scores):.2%}')

    era_scores.rolling(10).mean().plot(kind='line', title='Rolling Per Era Correlation Mean', figsize=(15,4))
    plt.axhline(y=0.0, color="r", linestyle="--"); plt.show()

    era_scores.cumsum().plot(title='Cumulative Sum of Era Scores', figsize=(15,4))
    plt.axhline(y=0.0, color="r", linestyle="--"); plt.show()
