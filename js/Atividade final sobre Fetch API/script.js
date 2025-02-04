document.addEventListener('DOMContentLoaded', function() {
    const lista = document.getElementById('lista');
    const modal = document.getElementById('modal');
    const info = document.getElementById('info');
    const fechar = modal.querySelector('.btn-close');

    carregar();

    async function carregar() {
        try {
            let resPosts = await fetch('https://jsonplaceholder.typicode.com/posts');
            let posts = await resPosts.json();
            
            let resUsers = await fetch('https://jsonplaceholder.typicode.com/users');
            let users = await resUsers.json();
            
            lista.innerHTML = '';
            
            for(let i = 0; i < 10; i++) {
                if(posts[i]) {
                    let user = users.find(u => u.id === posts[i].userId);
                    criar(posts[i], user);
                }
            }
        } catch(erro) {
            lista.innerHTML = `<div class="alert alert-danger">Erro ao carregar: ${erro.message}</div>`;
        }
    }

    function criar(post, user) {
        if (post.title && post.body && user) {
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
            lista.innerHTML += itemHtml;
        }
    }

    window.detalhes = async function(id) {
        try {
            info.innerHTML = '<div class="text-center"><div class="spinner-border"></div></div>';
            
            let res = await fetch(`https://jsonplaceholder.typicode.com/comments?postId=${id}`);
            let comentarios = await res.json();
            
            let infoHtml = '';
            for (let comentario of comentarios) {
                infoHtml += `
                    <div class="coment">
                        <h6>${comentario.name}</h6>
                        <p><strong>Email:</strong> ${comentario.email}</p>
                        <p>${comentario.body}</p>
                    </div>
                `;
            }
            
            info.innerHTML = infoHtml || '<div class="alert alert-warning">Nenhum comentário encontrado.</div>';
            modal.classList.add('show');
            modal.style.display = 'block';
        } catch(erro) {
            info.innerHTML = `<div class="alert alert-danger">Erro ao carregar: ${erro.message}</div>`;
        }
    }

    fechar.addEventListener('click', function() {
        modal.classList.remove('show');
        modal.style.display = 'none';
    });
});
