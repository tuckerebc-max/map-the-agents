# Git Branch Display Implementation Plan

## Overview
Add git branch information to the Repository File Viewer component to display the current branch name in the UI. This will help users understand which branch they're working on when viewing repository files.

## Current Architecture Analysis

### Frontend Structure
- **React-based SPA** located in `/frontend/src/`
- **Repository File Viewer**: `/frontend/src/components/RepositoryFileViewer.js`
- **Repository Selector**: `/frontend/src/components/RepositorySelector.js`
- **API Communication**: Uses axios with base URL from `/frontend/src/config/api`
- **State Management**: Local component state with session storage for persistence

### Backend Structure
- **FastAPI server** in `/backend/main.py`
- **Current endpoints**: `/directories`, `/tree`, `/file_content`, etc.
- **No existing git integration** - only file system operations
- **Repository path**: Configured via `REPO_PATH` environment variable

## Implementation Strategy

### Phase 1: Backend Implementation

#### 1.1 Create Git Utility Module
**File**: `/backend/utils/git_operations.py`

```python
import subprocess
import os
from typing import Optional, Dict

def get_git_info(repo_path: str) -> Dict[str, Optional[str]]:
    """
    Get git information for a repository.
    Returns dict with branch, commit_hash, and any errors.
    """
    try:
        # Check if it's a git repository
        if not os.path.exists(os.path.join(repo_path, '.git')):
            return {"branch": None, "commit_hash": None, "error": "Not a git repository"}
        
        # Get current branch name
        result = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            cwd=repo_path,
            capture_output=True,
            text=True,
            timeout=5
        )
        
        if result.returncode == 0:
            branch = result.stdout.strip()
            
            # Get current commit hash (short)
            commit_result = subprocess.run(
                ["git", "rev-parse", "--short", "HEAD"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                timeout=5
            )
            
            commit_hash = commit_result.stdout.strip() if commit_result.returncode == 0 else None
            
            return {
                "branch": branch,
                "commit_hash": commit_hash,
                "error": None
            }
        else:
            return {
                "branch": None,
                "commit_hash": None,
                "error": f"Git command failed: {result.stderr.strip()}"
            }
            
    except subprocess.TimeoutExpired:
        return {"branch": None, "commit_hash": None, "error": "Git command timeout"}
    except Exception as e:
        return {"branch": None, "commit_hash": None, "error": str(e)}
```

#### 1.2 Add Git API Endpoint
**File**: `/backend/main.py`

Add import:
```python
from utils.git_operations import get_git_info
```

Add new endpoint:
```python
@app.get("/git-info/{repository}")
async def get_repository_git_info(repository: str):
    """Get git information for a specific repository."""
    try:
        repo_path = os.path.join(REPO_PATH, repository)
        
        if not os.path.exists(repo_path):
            raise HTTPException(status_code=404, detail="Repository not found")
        
        git_info = get_git_info(repo_path)
        return git_info
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get git info: {str(e)}")
```

### Phase 2: Frontend Implementation

#### 2.1 Update Repository Selector Component
**File**: `/frontend/src/components/RepositorySelector.js`

Add state for git information:
```javascript
const [gitInfo, setGitInfo] = useState(null);
```

Add function to fetch git info:
```javascript
const fetchGitInfo = async (repository) => {
  if (!repository) {
    setGitInfo(null);
    return;
  }
  
  try {
    const response = await axios.get(`${API_URL}/git-info/${repository}`);
    setGitInfo(response.data);
  } catch (error) {
    console.error('Failed to fetch git info:', error);
    setGitInfo({ error: 'Failed to load git information' });
  }
};
```

Add effect to fetch git info when repository changes:
```javascript
useEffect(() => {
  fetchGitInfo(selectedRepository);
}, [selectedRepository]);
```

Update the render to include git branch display:
```javascript
// Add this after the repository select dropdown and before context map info
{selectedRepository && gitInfo && (
  <div className="mt-2 flex items-center gap-2">
    <span className="text-xs text-gray-600 dark:text-gray-400">Branch:</span>
    <span className="inline-flex items-center px-2 py-1 rounded-full text-xs font-medium bg-green-100 text-green-800 dark:bg-green-800 dark:text-green-100">
      <svg className="w-3 h-3 mr-1" fill="currentColor" viewBox="0 0 16 16">
        <path fillRule="evenodd" d="M11.75 2.5a.75.75 0 100 1.5.75.75 0 000-1.5zm-2.25.75a2.25 2.25 0 113 2.122V6A2.5 2.5 0 0110 8.5H6a1 1 0 00-1 1v1.128a2.251 2.251 0 11-1.5 0V9.5A2.5 2.5 0 016 7h4a1 1 0 001-1V4.372A2.25 2.25 0 019.5 3.25zM4.25 12a.75.75 0 100 1.5.75.75 0 000-1.5z"/>
      </svg>
      {gitInfo.branch || 'Unknown'}
    </span>
    {gitInfo.commit_hash && (
      <span className="text-xs text-gray-500 dark:text-gray-400">
        @ {gitInfo.commit_hash}
      </span>
    )}
  </div>
)}

{selectedRepository && gitInfo?.error && (
  <div className="mt-2 text-xs text-red-500 dark:text-red-400">
    {gitInfo.error}
  </div>
)}
```

#### 2.2 Alternative: Update Repository File Viewer Header
**File**: `/frontend/src/components/RepositoryFileViewer.js`

If we want the git branch in the file viewer header instead of the selector:

Add state and fetch logic similar to above, then update the header section:
```javascript
// In the sticky header section, update the title area:
<div className="flex justify-between items-center mb-2">
  <div className="flex items-center gap-3">
    <h3 className="text-base font-bold">Repository Structure</h3>
    {gitInfo?.branch && (
      <span className="inline-flex items-center px-2 py-1 rounded-full text-xs font-medium bg-green-100 text-green-800 dark:bg-green-800 dark:text-green-100">
        <svg className="w-3 h-3 mr-1" fill="currentColor" viewBox="0 0 16 16">
          <path fillRule="evenodd" d="M11.75 2.5a.75.75 0 100 1.5.75.75 0 000-1.5zm-2.25.75a2.25 2.25 0 113 2.122V6A2.5 2.5 0 0110 8.5H6a1 1 0 00-1 1v1.128a2.251 2.251 0 11-1.5 0V9.5A2.5 2.5 0 016 7h4a1 1 0 001-1V4.372A2.25 2.25 0 019.5 3.25zM4.25 12a.75.75 0 100 1.5.75.75 0 000-1.5z"/>
        </svg>
        {gitInfo.branch}
      </span>
    )}
  </div>
  <button ... // existing show/hide excluded files button
</div>
```

## Security Considerations

### 1. Input Validation
- Repository names must be validated to prevent path traversal
- Only allow alphanumeric characters, hyphens, and underscores in repository names

### 2. Command Execution Safety
- Use subprocess with explicit timeout (5 seconds)
- Limit to read-only git commands (`git rev-parse`, `git branch`)
- No user input directly passed to git commands
- Repository path is validated before git command execution

### 3. Error Handling
- Graceful degradation when git is not available
- Clear error messages for non-git repositories
- Timeout handling for slow git operations

## Implementation Order

1. **Backend**: Create git utility module (`/backend/utils/git_operations.py`)
2. **Backend**: Add git-info endpoint to main.py
3. **Frontend**: Update RepositorySelector to fetch and display git info
4. **Testing**: Test with various repository states (normal, detached HEAD, non-git repos)
5. **Polish**: Add loading states and better error handling

## Files to Modify

### New Files
- `/backend/utils/git_operations.py` - Git utility functions

### Modified Files
- `/backend/main.py` - Add git-info endpoint
- `/frontend/src/components/RepositorySelector.js` - Display git branch info

### Alternative Modified Files (if showing in file viewer instead)
- `/frontend/src/components/RepositoryFileViewer.js` - Display git branch in header

## Design Decisions

### Location Choice: Repository Selector vs File Viewer
**Recommendation**: Display in **Repository Selector** component

**Reasoning**:
1. **Semantic Alignment**: Git branch is repository-level metadata, fits naturally with repository selection
2. **Always Visible**: Branch info remains visible even when scrolling through files
3. **Context**: Users see branch info immediately upon selecting a repository
4. **Less Clutter**: Keeps file viewer header focused on file operations

### Visual Design
- **Badge Style**: Green rounded badge with git branch icon
- **Compact Layout**: Small, unobtrusive display
- **Dark Mode**: Proper contrast for both light and dark themes
- **Error States**: Subtle red text for git errors

## Testing Strategy

### Test Cases
1. **Normal Git Repository**: Shows current branch name and commit hash
2. **Detached HEAD**: Shows commit hash instead of branch name
3. **Non-Git Repository**: Shows "Not a git repository" message
4. **Git Command Failure**: Shows appropriate error message
5. **Repository Not Found**: Returns 404 error
6. **Network/Timeout**: Handles timeout gracefully

### Manual Testing
1. Test with various branch names (including special characters)
2. Test switching between repositories with different git states
3. Test UI responsiveness during git info loading
4. Verify dark mode styling

## Future Enhancements

### Phase 2 Potential Features
1. **Git Status Indicators**: Show if repository has uncommitted changes
2. **Branch Switching**: Allow branch switching from UI
3. **Commit History**: Show recent commits
4. **Remote Info**: Display remote repository information
5. **Refresh Button**: Manual refresh of git information

### Performance Optimizations
1. **Caching**: Cache git info for short periods to reduce git command frequency
2. **Background Refresh**: Update git info in background when files change
3. **Debouncing**: Debounce rapid repository switches

This implementation provides a solid foundation for git integration while maintaining security and user experience best practices.