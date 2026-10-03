# 💻 Guia Prático de Inclusão de Código-Fonte em LaTeX (Listings & Minted)

Este guia faz parte do acervo de referências do **Aluno Nota 90** para a elaboração de trabalhos, relatórios de programação e projetos das disciplinas de computação e engenharia.

---

## 1. O Pacote `listings` (Padrão Nativo, Sem Dependências Externas)

O `listings` é a escolha padrão porque compila diretamente em qualquer instalação do LaTeX (pdflatex, xelatex, Overleaf) sem exigir Python ou binários externos instalados.

### ⚠️ O Truque de Mestre: Acentuação em Português nos Comentários
Por padrão, o `listings` quebra a compilação se houver acentos em comentários (ex: `// cálculo de área`). Para resolver isso de forma definitiva, adicione a configuração `literate` no preâmbulo:

```latex
\usepackage{listings}
\usepackage{xcolor}

\lstset{
  extendedchars=true,
  literate={á}{{\'a}}1 {é}{{\'e}}1 {í}{{\'i}}1 {ó}{{\'o}}1 {ú}{{\'u}}1
           {Á}{{\'A}}1 {É}{{\'E}}1 {Í}{{\'I}}1 {Ó}{{\'O}}1 {Ú}{{\'U}}1
           {à}{{\`a}}1 {è}{{\`e}}1 {ì}{{\`i}}1 {ò}{{\`o}}1 {ù}{{\`u}}1
           {ã}{{\~a}}1 {õ}{{\~o}}1 {Ã}{{\~A}}1 {Õ}{{\~O}}1
           {ç}{{\c{c}}}1 {Ç}{{\c{C}}}1
           {ê}{{\^e}}1 {ô}{{\^o}}1 {Ê}{{\^E}}1 {Ô}{{\^O}}1
}
```

---

## 2. Configurações Prontas por Linguagem

### 🐍 Python
```latex
\begin{lstlisting}[language=Python, caption={Algoritmo de Fatoração.}, label={lst:python_ex}]
def fibonacci(n: int) -> int:
    # Caso base da recursão
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
\end{lstlisting}
```

### ☕ Java
```latex
\begin{lstlisting}[language=Java, caption={Classe de Conexão JDBC.}, label={lst:java_ex}]
public class DatabaseManager {
    private static final String URL = "jdbc:postgresql://localhost:5432/faculdade";
    
    public Connection connect() throws SQLException {
        // Inicializa o pool de conexões
        return DriverManager.getConnection(URL, "usuario", "senha");
    }
}
\end{lstlisting}
```

### 🗄️ SQL (Banco de Dados Relacionais)
```latex
\begin{lstlisting}[language=SQL, caption={Consulta com JOIN e Agregação.}, label={lst:sql_ex}]
SELECT 
    d.nome AS departamento,
    COUNT(f.id) AS total_funcionarios,
    AVG(f.salario) AS media_salarial
FROM departamento d
LEFT JOIN funcionario f ON f.id_departamento = d.id
GROUP BY d.nome
HAVING COUNT(f.id) > 5
ORDER BY media_salarial DESC;
\end{lstlisting}
```

### ⚡ TypeScript / JavaScript
```latex
\begin{lstlisting}[language=JavaScript, caption={Função assíncrona com Promise.}, label={lst:js_ex}]
async function fetchStudentGrades(studentId: string): Promise<GradeRecord[]> {
  // Chamada de API com tratamento de exceções
  const response = await fetch(`/api/grades/${studentId}`);
  if (!response.ok) {
    throw new Error("Erro ao buscar histórico do aluno");
  }
  return response.json();
}
\end{lstlisting}
```

---

## 3. O Pacote `minted` (Para Realce de Sintaxe Perfeito / Pygments)

Se você quiser realce de sintaxe idêntico ao do VS Code, use o pacote `minted`:
- **Vantagem:** Utiliza a biblioteca `Pygments` do Python; suporte a mais de 300 linguagens e dezenas de temas visuais (Monokai, Solarized, Gruvbox, etc.).
- **Requisito de Compilação:** Exige a flag `-shell-escape` ao rodar o compilador:
  ```bash
  pdflatex -shell-escape meu_documento.tex
  ```

### Exemplo com `minted`:
```latex
\usepackage{minted}
\usemintedstyle{monokai}

\begin{minted}[
  frame=lines,
  framesep=2mm,
  baselinestretch=1.2,
  bgcolor=black,
  fontsize=\footnotesize,
  linenos
]{python}
import numpy as np

def sigmoid(z):
    """Calcula a função sigmóide para aprendizado de máquina."""
    return 1.0 / (1.0 + np.exp(-z))
\end{minted}
```

---

## 4. Como Carregar Código Diretamente de Arquivos Externos

Em vez de copiar e colar código longo no `.tex`, você pode referenciar o arquivo real do projeto:

```latex
% Usando listings:
\lstinputlisting[language=Python, caption={Arquivo de configuração completo.}]{scripts/config.py}

% Usando minted:
\inputminted{python}{scripts/config.py}
```
Isso garante que, quando você atualizar o código do seu trabalho, o PDF do LaTeX será atualizado automaticamente ao recompilar!
