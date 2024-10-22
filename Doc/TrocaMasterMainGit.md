Excluindo .git
    Resumo dos passos:
    Excluir a pasta .git.
    Iniciar um novo repositório com git init.
    Adicionar arquivos com git add ..
    Fazer o primeiro commit com git commit -m "Primeiro commit".
    (Opcional) Adicionar repositório remoto e fazer o git push.
    Com isso, você começa do zero com um novo repositório Git no seu projeto.

###---------------------------------------------------------------

Para mudar a branch principal do Git de `master` para `main` e aplicar isso em um único repositório, siga os passos abaixo:

### 1. Renomear a branch local
Se sua branch local ainda se chama `master`, você pode renomeá-la para `main` com o seguinte comando:

```bash
git branch -m master main
```

### 2. Atualizar o repositório remoto
Agora, você precisa configurar o Git para que a nova branch principal seja enviada para o repositório remoto:

```bash
git push -u origin main
```

Este comando empurra a branch `main` para o repositório remoto e define-a como a branch padrão para futuros `push` e `pull`.

### 3. Alterar a branch padrão no GitHub ou repositório remoto
Se você estiver usando GitHub ou outro serviço de hospedagem de repositórios:

- No GitHub, vá até o repositório, clique em **Settings**, depois em **Branches** e mude a branch padrão para `main`.
  
### 4. Deletar a branch antiga `master`
Se não houver mais necessidade da branch `master`, você pode deletá-la no repositório remoto:

```bash
git push origin --delete master
```

Isso garante que o repositório remoto não tenha mais a branch `master`.

### 5. Atualizar repositórios locais dos colaboradores
Para outros colaboradores que clonaram o repositório antes da mudança, eles podem atualizar o repositório local executando os comandos abaixo:

```bash
git fetch origin
git branch -u origin/main main
git symbolic-ref refs/remotes/origin/HEAD refs/remotes/origin/main
```

Isso garante que o Git local de cada colaborador esteja atualizado e aponte corretamente para `main` como a nova branch padrão.

Agora, seu repositório está totalmente configurado para usar `main` como branch principal, tanto local quanto remotamente.