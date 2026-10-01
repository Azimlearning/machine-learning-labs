# Environment Setup — TEB3123 Machine Learning

> **Security:** never commit a real value from this file. `.env*` and SSH keys are gitignored; the SSH *private* key never leaves `~/.ssh`.
> Never paste a private key or token into a plan, an execution doc, a changelog entry, or a chat transcript. If one leaks, rotate it — don't just delete the message.

Last updated: 2026-10-01

---

## Required variables

No environment variables yet — add the first one here and to `.env.example` in the same commit.

---

## Setup

Open **Anaconda PowerShell Prompt** from the Start menu (`conda` is not on PATH in a normal terminal), then:

```powershell
conda create -n ml python=3.12      # once
conda activate ml                   # every session
cd "C:\Users\User\Documents\UTP COURSE\Machine Learning\ML LAB"
pip install -r requirements.txt     # once, after activating
python -c "import sys; print(sys.executable)"   # must point inside ...\envs\ml
```

Rules from the lab notes: create once, activate every session, never install into `base`, never install the same package with both conda and pip. Recreate a broken env with `conda env remove -n ml`, then repeat. If Jupyter fails to import, activate `ml`, restart Jupyter and re-check the kernel.

Datasets: download manually from the links in `ML LAB/all_datasets/README.md` into `ML LAB/all_datasets/`. Keep the digits ZIP intact.

### GitHub SSH (weekend task, TA, 2026-09-25/26)

Follow the TA's Windows video (see sources, A-09). The standard procedure, for cross-checking against the video:

```powershell
ssh-keygen -t ed25519 -C "<your GitHub email>"      # accept default path; set a passphrase
Get-Service ssh-agent | Set-Service -StartupType Manual   # admin PowerShell, once
Start-Service ssh-agent
ssh-add $env:USERPROFILE\.ssh\id_ed25519
Get-Content $env:USERPROFILE\.ssh\id_ed25519.pub | Set-Clipboard   # PUBLIC key only
```

Paste it at GitHub → Settings → SSH and GPG keys → New SSH key, then test with `ssh -T git@github.com` (expect "Hi <username>! You've successfully authenticated"). Full steps with verification: `refdocs/execution/2026-10-01-p0-environment-and-github.md`.

---

## Rules

- **`.env.example` is the documentation.** If a variable is ever added, add its name there the moment you add it.
- **A missing required variable should fail loudly at startup**, with a message naming the variable and pointing here.
- **Rotate on exposure, not on suspicion of exposure.** If a private key or token may have left the machine, treat it as leaked.
- **Only the `.pub` file is ever copied or pasted.** The file without the extension is the private key.

## When setup changes

Adding, renaming or removing a package means updating `ML LAB/requirements.txt`, this file if the steps change, and a changelog entry in the same session.
