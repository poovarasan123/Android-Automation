# Android Clean Architecture Setup

This project helps automate the creation of a Clean Architecture folder structure in an Android project. The script provides the following features:

- Locates key project files like `build.gradle`, `AndroidManifest.xml`.
- Creates a Clean Architecture folder structure with appropriate subfolders.
- Adds README files to explain the purpose of each Clean Architecture layer.
- Updates the `AndroidManifest.xml` file with the required permissions.
- Adds essential dependencies in the `build.gradle` or `libs.versions.toml` files.

## Features

### 1. **Clean Architecture Folder Structure**
   The folder structure includes:
   - **Domain Layer**: Contains business logic and domain models.
   - **Data Layer**: Handles data operations (repositories, local data sources, remote data sources).
   - **Presentation Layer**: Manages the UI, activities, fragments, view models, etc.

### 2. **Add Permissions to AndroidManifest.xml**
   The script allows you to select from different permission categories such as:
   - **Basic**
   - **Beginner**
   - **Intermediate**
   - **Advanced**

   These permissions will be automatically added to the `AndroidManifest.xml` file.

### 3. **Add Dependencies**
   The script adds dependencies for essential libraries like Glide and Dagger Hilt. You can choose between two methods:
   - **Method 1**: Directly adding dependencies to the `build.gradle` file.
   - **Method 2**: Adding dependencies with versions to the `libs.versions.toml` file.

## Requirements

- Python 3.x
- An Android project with an existing `build.gradle` file

## Setup Instructions

1. Clone or download the script into your project folder.
2. Run the script:
   - Ensure your Android project folder is specified.
   - The script will guide you through selecting permission categories and adding dependencies.
   
3. The script will:
   - Create a Clean Architecture folder structure.
   - Add necessary README files to explain each layer.
   - Update the `AndroidManifest.xml` with permissions.
   - Add dependencies to the `build.gradle` or `libs.versions.toml` file.

## Example Output

- A new folder structure will be created under `app/src/main/java/{package_name}`.
- Each layer (domain, data, presentation) will have its own `README.md` file.
- The selected permissions will be added to the `AndroidManifest.xml`.
- Dependencies will be appended to the appropriate Gradle files.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
