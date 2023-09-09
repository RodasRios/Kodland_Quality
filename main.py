from modules import data_loading, data_cleaning, data_preprocessing, model_building

def main():
    # Load the dataset
    df_raw = data_loading.load_dataset('D:/Python proj/Kodland_Quality/Datasets/MENA_RAW.csv')
    
    # Perform data cleaning
    df_cleaned = data_cleaning.clean_data(df_raw)
    
    # Perform data preprocessing
    X_train, X_test, y_train, y_test, X = data_preprocessing.preprocess_data(df_cleaned)
    
    # Build and evaluate the model
    model = model_building.build_model(X_train,y_train)
    model_building.evaluate_model(model, y_test, X_test, X)

if __name__ == "__main__":
    main()