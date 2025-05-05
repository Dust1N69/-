# Booking Prediction

## 專案背景
本專案旨在根據訪客的流量統計資料，預測其是否會進行消費。

## 資料來源
- `train.csv`: 訓練資料，包含訪客的流量特徵與消費標籤。
- `test.csv`: 測試資料，需預測訪客的消費機率。
- `sample_submission.csv`: 提交格式範例。

## 分析與建模過程
1. **資料分析與視覺化**:
   - 檢查資料分佈與缺失值。
   - 分析特徵與目標變數的相關性。
   - 按月份與季節進行趨勢分析(附圖)。

2. **資料清理**:
   - 篩選出有意義的特徵欄位('Administrative','Informational','ProductRelated','PageValues','BounceRates','ExitRates','Month','VisitorType','Weekend','TrafficType')。
   - 類別特徵進行 One-Hot 編碼。
   - 數值特徵進行標準化。

3. **建模與評估**:
   - 使用多個模型(Logistic Regression, Random Forest, XGBoost, LightGBM)進行訓練與驗證。
   - 選擇 AUC 表現最佳的模型進行測試集預測。

## 結果
- 最佳模型: LightGBM (AUC = 0.9195, Accuracy = 0.8907)
- 提交結果已保存為 `my_submission1.csv`。

