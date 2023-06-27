

LOCK_OPTIONS = {
    'lock_epochs': 'u64',
    'penalty_start_percentage': 'u64'
}

ENERGY_ENTRY = {
    'amount': 'biguint',
    'last_update_epoch': 'u64',
    'total_locked_tokens': 'biguint',
}

ESDT_TOKEN_PAYMENT = {
    'token_identifier': 'string',
    'token_nonce': 'u64',
    'token_amount': 'biguint'
}

LIQUID_LOCKING_UNLOCKED_TOKEN = {
    'token_identifier': 'string',
    'token_nonce': 'u64',
    'unbond_epoch': 'biguint',
    'unbond_epoch': 'u64',
}

LIQUID_LOCKING_LOCKED_TOKEN_AMOUNTS = {
    'locked_tokens': ESDT_TOKEN_PAYMENT
}

LIQUID_LOCKING_UNLOCKED_TOKEN_AMOUNTS = {
    'unlocked_tokens': LIQUID_LOCKING_UNLOCKED_TOKEN
}