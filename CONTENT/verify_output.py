
import os
import glob
import re

OUTPUT_DIR = r"c:\Users\ML Office\OneDrive - thepoweraddicts.ch\Projekte\PowerPlatformTip\CONTENT\2_OUTPUT"

def get_long_path(path):
    if os.name == 'nt' and not path.startswith('\\\\?\\'):
        return '\\\\?\\' + os.path.abspath(path)
    return path

def check_file_content(filepath, is_full_post=False):
    issues = []
    try:
        with open(get_long_path(filepath), 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Check for Share artifacts
            if "Share this:" in content or "class=\"sharedaddy\"" in content:
                issues.append("Contains 'Share' or 'sharedaddy' artifacts")
            
            # Check for Frontmatter in full post
            if is_full_post:
                if not content.startswith('---'):
                    issues.append("Missing Frontmatter")
                if "## 💡 Challenge" not in content and "## Problem" not in content:
                    issues.append("Missing 'Challenge' section")
            
            # Check for empty sections (simple heuristic)
            if "## 🔧 How It's Done\n\n\n" in content:
                issues.append("Empty 'How It's Done' section")

    except Exception as e:
        issues.append(f"Error reading file: {str(e)}")
    
    return issues

def verify_output():
    subdirs = [d for d in os.listdir(OUTPUT_DIR) if os.path.isdir(os.path.join(OUTPUT_DIR, d))]
    print(f"Verifying {len(subdirs)} directories...")
    
    total_issues = 0
    
    for subdir in subdirs:
        dir_path = os.path.join(OUTPUT_DIR, subdir)
        
        # Expected files
        expected_files = {
            "newsletter": "newsletter-systeme.md",
            "linkedin": "linkedin.md",
            "twitter": "twitter.md"
            # Full post filename is variable, usually YYYY-MM-DD-....md
        }
        
        found_files = os.listdir(dir_path)
        full_post_files = [f for f in found_files if f.endswith('.md') and f not in expected_files.values()]
        
        dir_issues = []
        
        # Check standard files
        for key, filename in expected_files.items():
            if filename not in found_files:
                dir_issues.append(f"Missing {filename}")
            else:
                filepath = os.path.join(dir_path, filename)
                file_issues = check_file_content(filepath)
                if file_issues:
                    dir_issues.append(f"{filename}: {', '.join(file_issues)}")

        # Check full post file
        if not full_post_files:
            dir_issues.append("Missing Full Blog Post file")
        elif len(full_post_files) > 1:
            dir_issues.append(f"Multiple potential blog post files: {full_post_files}")
        else:
            filepath = os.path.join(dir_path, full_post_files[0])
            file_issues = check_file_content(filepath, is_full_post=True)
            if file_issues:
                 dir_issues.append(f"Full Post ({full_post_files[0]}): {', '.join(file_issues)}")

        if dir_issues:
            total_issues += 1
            print(f"\nIssues in {subdir}:")
            for issue in dir_issues:
                print(f"  - {issue}")
    
    if total_issues == 0:
        print("\nAll directories verified successfully! No issues found.")
    else:
        print(f"\nFound issues in {total_issues} directories.")

if __name__ == "__main__":
    verify_output()
