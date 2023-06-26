<template>
  <div>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <!-- Conteúdo da navbar aqui -->
    </nav>
    <div class="container-fluid">
      <div class="row">
        <div class="col-lg-3 px-0" style="padding:0;">
          <div class="col-lg-9 px-0" style="padding:0;">
            <div class="sidebar">
              <ul class="menu">
                <li class="menu-item">
                  <div class="row justify-content-center align-items-center">
                    <div class="col-lg-3">
                      <div class="menu-item-icon">
                          sds
                      </div>
                    </div>
                    <div class="col-lg-9">
                      <a href="#" class="menu-link">Home</a>
                    </div>
                  </div>
                </li>
                <li class="menu-item"><a href="#" class="menu-link">Usuários</a></li>
                <!-- Adicione mais itens conforme necessário -->
              </ul>
            </div>
          </div>
        </div>
        <div class="col-lg-9">
          <div class="main-content">
            <!-- Conteúdo principal aqui -->
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import icon from './icons/Icon.vue'
export default {
  name: 'Dashboard',
  components: {
    icon,
  }
}
</script>

<style>
.sidebar {
  background-color: #f8f9fa;
  height: 100vh;
  padding: 20px;
}

.menu {
  list-style-type: none;
  padding: 0;
  width: 100%;
}

.menu-item {
  background-color: #e9ecef;
  margin-bottom: 10px;
  border-radius: 20px;
}

.menu-item a {
  color: #000;
  text-decoration: none;
  padding: 10px;
}

.menu-item a:hover {
  color: #fff;
}

.menu-link {
  display: block;
  background-color: #e9ecef;
  /* Cor de fundo para cada item do menu */
  color: #000;
  text-decoration: none;
  border-radius: 20px;
}

.menu-link:hover {
  background-color: #ff0040;
  /* Cor de fundo ao passar o mouse */
  color: #fff;
  /* Cor do texto ao passar o mouse */
}
</style>
