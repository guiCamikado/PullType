TABELA_INTRODUCAO(titulo, autor, data_criacao)
TABELA_DADOS(id_guia_vinculado, version, mod_name, mod_data, content)

TABLE_USERS(
    id              Int primaryKey,
    username        String,
    email           String,
    name            String,
    last_name       String,
    password        String,
    user_born_in    date,
    recovery_key    string,
    account_created date,
    last_section    date,
    google_oAuth    bool
    )

TABLE_GUIDES(
    id
    name
    
)