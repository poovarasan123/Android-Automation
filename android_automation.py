import os
import re
import xml.etree.ElementTree as ET
from xml.dom import minidom


def find_build_gradle(base_path):
    """
    Locate the build.gradle or build.gradle.kts file in the 'app' folder under the base path.
    Automatically appends 'app' to the base path if not already included.
    """
    # Ensure the path includes 'app'
    app_folder = os.path.join(base_path, "app")
    
    for root, _, files in os.walk(app_folder):
        for file in files:
            if file in ("build.gradle", "build.gradle.kts"):
                return os.path.join(root, file)
    return None


def extract_application_id(gradle_file):
    """
    Extract the applicationId from the build.gradle or build.gradle.kts file.
    """
    try:
        with open(gradle_file, "r") as file:
            content = file.read()
            match = re.search(r'applicationId\s*=\s*"([^"]+)"', content)
            if match:
                return match.group(1)
    except Exception as e:
        return f"Error reading gradle file: {e}"
    return "applicationId not found"


def create_readme(folder_path, content):
    """
    Create a README.md file in a folder to explain its purpose.
    """
    try:
        readme_path = os.path.join(folder_path, "README.md")
        with open(readme_path, "w") as readme_file:
            readme_file.write(content)
        print(f"README created at: {readme_path}")
    except Exception as e:
        print(f"Error creating README: {e}")


def create_folders(base_path, package_name):
    """
    Create a Clean Architecture folder structure for an Android project.
    """
    print(f"Package name: {package_name}")
    try:
        # Replace dots in the package name with slashes to create folder structure
        package_path = package_name.replace(".", "/")
        # Define the folder structure
        folders = [
            os.path.join(base_path, f"app/src/main/java/{package_path}"),
            os.path.join(base_path, f"app/src/main/java/{package_path}/domain"),
            os.path.join(base_path, f"app/src/main/java/{package_path}/domain/models"),
            os.path.join(base_path, f"app/src/main/java/{package_path}/domain/usecases"),
            os.path.join(base_path, f"app/src/main/java/{package_path}/data"),
            os.path.join(base_path, f"app/src/main/java/{package_path}/data/repository"),
            os.path.join(base_path, f"app/src/main/java/{package_path}/data/local"),
            os.path.join(base_path, f"app/src/main/java/{package_path}/data/remote"),
            os.path.join(base_path, f"app/src/main/java/{package_path}/presentation"),
            os.path.join(base_path, f"app/src/main/java/{package_path}/presentation/ui"),
            os.path.join(base_path, f"app/src/main/java/{package_path}/presentation/viewmodels"),
        ]

        # Create folders
        for folder in folders:
            os.makedirs(folder, exist_ok=True)

        print(f"Clean Architecture folder structure created successfully at {base_path}")
    except Exception as e:
        print(f"Error creating folders: {e}")


def add_readmes(base_path, package_name):
    """
    Add README.md files to explain each layer in Clean Architecture.
    """
    readme_contents = {
        "domain": "This layer contains business logic and domain models.\n\n- `models`: Define core business objects.\n- `usecases`: Represent operations the application can perform.",
        "data": "This layer handles data operations.\n\n- `repository`: Interfaces and implementations for data access.\n- `local`: Local data sources, like Room database.\n- `remote`: Remote data sources, like APIs.",
        "presentation": "This layer manages the UI and user interaction.\n\n- `ui`: Activities, Fragments, and Composable.\n- `viewmodels`: ViewModels for managing UI-related data.",
    }

    package_path = package_name.replace(".", "/")

    for layer, content in readme_contents.items():
        folder_path = os.path.join(base_path, f"app/src/main/java/{package_path}/{layer}")
        create_readme(folder_path, content)


def find_manifest_file(base_path):
    """
    Locate the AndroidManifest.xml file in the app folder.
    """
    manifest_path = os.path.join(base_path, "app/src/main/AndroidManifest.xml")
    return manifest_path if os.path.exists(manifest_path) else None


def add_permissions(manifest_path, permissions):
    """
    Add permissions to the AndroidManifest.xml file.
    """
    try:
        tree = ET.parse(manifest_path)
        root = tree.getroot()

        # Android namespace
        android_ns = "http://schemas.android.com/apk/res/android"
        ET.register_namespace("android", android_ns)

        # Check existing permissions
        existing_permissions = {elem.get(f"{{{android_ns}}}name") for elem in root.findall("uses-permission")}

        added_permissions = []
        for permission in permissions:
            if permission not in existing_permissions:
                ET.SubElement(root, "uses-permission", {f"{{{android_ns}}}name": permission})
                added_permissions.append(permission)

        # Save changes
        if added_permissions:
            tree.write(manifest_path, encoding="utf-8", xml_declaration=True)
            print(f"Added permissions: {', '.join(added_permissions)}")
        else:
            print("All permissions already exist in the AndroidManifest.xml file.")

    except Exception as e:
        print(f"Error updating AndroidManifest.xml: {e}")


def main(app_folder):
    permissions = {
        "basic": [
            "android.permission.INTERNET",
            "android.permission.ACCESS_NETWORK_STATE",
            "android.permission.ACCESS_WIFI_STATE",
            "android.permission.READ_EXTERNAL_STORAGE"
        ],
        "beginner": [
            "android.permission.INTERNET",
            "android.permission.ACCESS_NETWORK_STATE",
            "android.permission.ACCESS_WIFI_STATE",
            "android.permission.READ_EXTERNAL_STORAGE",
            "android.permission.CAMERA",
            "android.permission.ACCESS_FINE_LOCATION",
            "android.permission.BLUETOOTH"
        ],
        "intermediate": [
        	"android.permission.INTERNET",
            "android.permission.ACCESS_NETWORK_STATE",
            "android.permission.ACCESS_WIFI_STATE",
            "android.permission.READ_EXTERNAL_STORAGE",
            "android.permission.CAMERA",
            "android.permission.ACCESS_FINE_LOCATION",
            "android.permission.BLUETOOTH",
            "android.permission.READ_SMS",
            "android.permission.WRITE_SETTINGS",
            "android.permission.BLUETOOTH_ADMIN",
            "android.permission.ACCESS_COARSE_LOCATION"
        ],
        "advanced": [
        	"android.permission.INTERNET",
            "android.permission.ACCESS_NETWORK_STATE",
            "android.permission.ACCESS_WIFI_STATE",
            "android.permission.READ_EXTERNAL_STORAGE",
            "android.permission.CAMERA",
            "android.permission.ACCESS_FINE_LOCATION",
            "android.permission.BLUETOOTH",
            "android.permission.READ_SMS",
            "android.permission.WRITE_SETTINGS",
            "android.permission.BLUETOOTH_ADMIN",
            "android.permission.ACCESS_COARSE_LOCATION",
            "android.permission.USE_BIOMETRIC",
            "android.permission.INSTALL_PACKAGES",
            "android.permission.REQUEST_INSTALL_PACKAGES"
        ]
    }

    # Prompt the user for category choice
    print("Select the permission category to add:")
    print("1. Basic")
    print("2. Beginner")
    print("3. Intermediate")
    print("4. Advanced")
    

    category_choice = input("Enter your choice (1/2/3/4): ").strip()

    # Map user choice to corresponding permissions
    if category_choice == "1":
        selected_permissions = permissions["basic"]
    elif category_choice == "2":
        selected_permissions = permissions["beginner"]
    elif category_choice == "3":
        selected_permissions = permissions["intermediate"]
    elif category_choice == "4":
        selected_permissions = permissions["advanced"]
    else:
        print("Invalid choice! Exiting...")
        return

    # # Get the base path for the Android project
    # app_folder = input("Enter the path to your Android app folder: ").strip()

    # Find the AndroidManifest.xml file
    manifest_file = find_manifest_file(app_folder)
    
    if manifest_file:
        print(f"Manifest file found at: {manifest_file}")
        
        # Confirm permissions with the user
        print("The following permissions will be added:")
        for permission in selected_permissions:
            print(f"- {permission}")
        
        confirm = input("Do you want to add these permissions? (yes/no): ").strip().lower()
        if confirm in ("yes", "y"):
            add_permissions(manifest_file, selected_permissions)
        else:
            print("Permission addition skipped.")
    else:
        print("Manifest file not found in the specified app folder.")



def add_dependencies_method_1(build_gradle_file):
    """
    Adds dependencies using method 1 (directly specifying versions) in the build.gradle file.
    Prompts for confirmation before adding each dependency.
    """
    dependencies = [
        "\t// Glide\n    implementation(\"com.github.bumptech.glide:glide:4.16.0\")\n",
        "\t// Lifecycle\n    implementation(\"androidx.lifecycle:lifecycle-runtime-ktx:2.6.1\")\n",
        "    implementation(\"androidx.lifecycle:lifecycle-viewmodel-ktx:2.6.1\")\n",
        "\t// Hilt\n    implementation(\"com.google.dagger:hilt-android:2.51.1\")\n",
        "    kapt(\"com.google.dagger:hilt-compiler:2.51.1\")\n",
        "\t// Retrofit & OkHttp\n    implementation(\"com.squareup.retrofit2:retrofit:2.9.0\")\n",
        "    implementation(\"com.squareup.okhttp3:okhttp:4.11.0\")\n",
        "\t// Room\n    implementation(\"androidx.room:room-runtime:2.6.0\")\n",
        "    kapt(\"androidx.room:room-compiler:2.6.0\")\n",
        "\t// Coroutine support\n    implementation(\"org.jetbrains.kotlinx:kotlinx-coroutines-android:1.7.3\")\n"
    ]

    try:
        with open(build_gradle_file, "r") as file:
            lines = file.readlines()

        # Find the dependencies block
        with open(build_gradle_file, "w") as file:
            inside_dependencies = False
            for line in lines:
                stripped_line = line.strip()

                # Check for the start of the dependencies block
                if stripped_line == "dependencies {":
                    inside_dependencies = True
                    file.write(line)  # Write the current line
                    # Prompt for each dependency
                    for dep in dependencies:
                        add_dependency = input(f"Do you want to add:\n{dep} (yes/no)? ").strip().lower()
                        if add_dependency in ['yes', 'y']:
                            file.write(f"{dep}\n")  # Write the dependency with proper formatting
                    continue

                # Check for the end of the dependencies block
                if inside_dependencies and stripped_line == "}":
                    inside_dependencies = False

                file.write(line)  # Write the line as is

        print("Dependencies successfully appended to the dependencies block where confirmed.")
    except Exception as e:
        print(f"Error adding dependencies in build.gradle: {e}")



def add_dependencies_method_2(libs_versions_toml_file):
    """
    Adds dependencies using method 2 (with versions in libs.versions.toml) to the libs.versions.toml file.
    """
    toml_content = """
[versions]
glide = "4.16.0"
hiltAndroid = "2.51.1"

[libraries]
hilt-android = { module = "com.google.dagger:hilt-android", version.ref = "hiltAndroid" }
hilt-android-compiler = { module = "com.google.dagger:hilt-android-compiler", version.ref = "hiltAndroid" }

[plugins]
dagger-hilt-android = { id = "com.google.dagger.hilt.android", version.ref = "hiltAndroid" }
    """
    
    try:
        # Open the file in append mode ('a') to avoid overwriting
        with open(libs_versions_toml_file, "a") as file:
            file.write("\n" + toml_content.strip() + "\n")
        print("Dependencies added using Method 2 in libs.versions.toml.")
    except Exception as e:
        print(f"Error adding dependencies in libs.versions.toml: {e}")



if __name__ == "__main__":
    # Specify your app folder
    app_folder = input("Enter the path to your app folder: ").strip()

    gradle_file = find_build_gradle(app_folder)

    if gradle_file:
        print(f"Gradle file found at: {gradle_file}")
        application_id = extract_application_id(gradle_file)

        if application_id and "not found" not in application_id:
            print(f"Extracted applicationId: {application_id}")
            confirmation = input(f"Is the applicationId '{application_id}' correct? (yes/no): ").strip().lower()
            if confirmation in ("yes", "y"):
                print("Confirmed!")

                # Create folder structure
                create_folders(app_folder, application_id)

                # Add README.md files to explain each layer
                add_readmes(app_folder, application_id)

                main(app_folder)

                build_gradle_file = os.path.join(app_folder, "app", "build.gradle.kts")
                libs_versions_toml_file = os.path.join(app_folder, "gradle", "libs.versions.toml")

                # Check if libs.versions.toml exists
                # if os.path.exists(libs_versions_toml_file):
                #     print("libs.versions.toml found. Using Method 2.")
                #     add_dependencies_method_2(libs_versions_toml_file)
                # else:
                print("libs.versions.toml not found. Using Method 1.")
                add_dependencies_method_1(build_gradle_file)

            else:
                print("Confirmation declined.")
        else:
            print("applicationId not found in the Gradle file.")
    else:
        print("build.gradle or build.gradle.kts file not found in the specified app folder.")
