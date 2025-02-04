// Ouvinte de evento para garantir que o código só será executado após a página estar totalmente carregada
document.addEventListener('DOMContentLoaded', function() {
    const lista = document.getElementById('lista');  // Referência ao elemento onde os posts serão exibidos
    const modal = document.getElementById('modal');  // Referência ao modal de comentários
    const info = document.getElementById('info');    // Referência ao conteúdo dentro do modal (onde os comentários serão carregados)
    const fechar = modal.querySelector('.btn-close'); // Referência ao botão de fechar o modal

    carregar();  // Chama a função para carregar os posts assim que a página for carregada

    // Função assíncrona para carregar os dados de posts e usuários
    async function carregar() {
        try {
            // Faz uma requisição para obter os posts
            let resPosts = await fetch('https://jsonplaceholder.typicode.com/posts');
            let posts = await resPosts.json(); // Converte a resposta para JSON
            
            // Faz uma requisição para obter os usuários
            let resUsers = await fetch('https://jsonplaceholder.typicode.com/users');
            let users = await resUsers.json(); // Converte a resposta para JSON
            
            lista.innerHTML = ''; // Limpa a lista de posts

            // Itera pelos primeiros 10 posts e cria os elementos para cada um
            for (let i = 0; i < 10; i++) {
                if (posts[i]) {
                    // Encontra o usuário correspondente ao post atual
                    let user = users.find(u => u.id === posts[i].userId);
                    criar(posts[i], user); // Chama a função para criar o HTML para o post
                }
            }
        } catch (erro) {
            // Exibe uma mensagem de erro caso algo dê errado
            lista.innerHTML = `<div class="alert alert-danger">Erro ao carregar: ${erro.message}</div>`;
        }
    }

    // Função para criar o HTML do post
    function criar(post, user) {
        if (post.title && post.body && user) {
            // Cria o HTML para o post com título, corpo e informações do autor
            let itemHtml = `
                <article class="item">
                    <div class="topo">
                        <div class="info">
                            <h5>${post.title}</h5>
                            <p>${post.body}</p>
                            <small><strong>${user.username}</strong> - ${user.email}</small>
                        </div>
                        <div class="acoes">
                            <button class="btn" onclick="detalhes(${post.id})">
                                <i class="fas fa-info-circle"></i>
                                <span>Comentários</span>
                            </button>
                        </div>
                    </div>
                </article>
            `;
            lista.innerHTML += itemHtml; // Adiciona o post à lista
        }
    }

    // Função que é chamada quando o usuário clica no botão de "Comentários"
    window.detalhes = async function(id) {
        try {
            // Exibe um ícone de carregamento enquanto os comentários estão sendo carregados
            info.innerHTML = '<div class="text-center"><div class="spinner-border"></div></div>';
            
            // Faz uma requisição para obter os comentários do post
            let res = await fetch(`https://jsonplaceholder.typicode.com/comments?postId=${id}`);
            let comentarios = await res.json(); // Converte a resposta para JSON
            
            let infoHtml = ''; // Variável para armazenar o HTML dos comentários
            // Itera sobre os comentários e cria o HTML para cada um
            for (let comentario of comentarios) {
                infoHtml += `
                    <div class="coment">
                        <h6>${comentario.name}</h6>
                        <p><strong>Email:</strong> ${comentario.email}</p>
                        <p>${comentario.body}</p>
                    </div>
                `;
            }
            
            // Exibe os comentários ou uma mensagem caso não haja comentários
            info.innerHTML = infoHtml || '<div class="alert alert-warning">Nenhum comentário encontrado.</div>';
            modal.classList.add('show'); // Exibe o modal
            modal.style.display = 'block'; // Mostra o modal com os comentários
        } catch (erro) {
            // Exibe uma mensagem de erro caso algo dê errado ao carregar os comentários
            info.innerHTML = `<div class="alert alert-danger">Erro ao carregar: ${erro.message}</div>`;
        }
    }

    // Evento para fechar o modal quando o usuário clicar no botão de fechar
    fechar.addEventListener('click', function() {
        modal.classList.remove('show'); // Remove a classe 'show' para esconder o modal
        modal.style.display = 'none'; // Esconde o modal
    });
});
