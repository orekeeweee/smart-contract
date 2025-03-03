# Smart Contract Vulnerability Detection

## Overview
This project implements a **hybrid detection framework** for identifying vulnerabilities in Solidity smart contracts. It leverages **signature-based detection** for known issues and **machine learning classification** to detect emerging threats.

## Features
- **Signature-Based Detection**: Uses predefined patterns to quickly detect known vulnerabilities.
- **Machine Learning Model**: Trained on a dataset of smart contracts using **Random Forest** and optimized via **GridSearchCV**.
- **Hybrid Approach**: Combines both methods to improve detection accuracy and reduce false negatives.

## How It Works
1. **Signature-Based Detection**: Scans for common security vulnerabilities.
2. **Machine Learning Classification**: Uses a trained model to detect complex patterns.
3. **Hybrid Decision System**: Ensures a more robust and adaptive detection mechanism.

## Performance
| Metric (%)  | Signature-Based | ML-Based | Hybrid |
|------------|----------------|----------|--------|
| **Accuracy**  | 62 | 70 | **88** |
| **Precision** | 75 | 73.9 | **95.2** |
| **Recall**    | 49 | 68.6 | **87.2** |
| **F1-Score**  | 36 | 64 | **80** |

## Future Improvements
- Expand the **signature-based detection** database.
- Improve **ML model performance** with advanced architectures.
- Test on **real-world smart contracts** for validation.
