from construct import Bytes, Int8ul, Int64ul, BytesInteger, Int32ul, Int16ul
from construct import Struct as cStruct 

"""Thanks to v0idum for creating layouts in python"""

POOL_INFO_LAYOUT = cStruct( 
    "instruction" / Int8ul,
    "simulate_type" / Int8ul
)

SWAP_LAYOUT = cStruct(
    "instruction" / Int8ul,
    "amount_in" / Int64ul,
    "min_amount_out" / Int64ul
)

# Not in use right now, might be useful in future
AMM_INFO_LAYOUT_V4 = cStruct(
    'status' / Int64ul,
    'nonce' / Int64ul,
    'order_num' / Int64ul,
    'depth' / Int64ul,
    'base_decimal' / Int64ul,
    'quote_decimal' / Int64ul,
    'state' / Int64ul,
    'reset_flag' / Int64ul,
    'min_size' / Int64ul,
    'vol_max_cut_ratio' / Int64ul,
    'amount_wave_ratio' / Int64ul,
    'base_lot_size' / Int64ul,
    'quote_lot_size' / Int64ul,
    'min_price_multiplier' / Int64ul,
    'max_price_multiplier' / Int64ul,
    'system_decimal_value' / Int64ul,
    # Fees
    'min_separate_numerator' / Int64ul,
    'min_separate_denominator' / Int64ul,
    'trade_fee_numerator' / Int64ul,
    'trade_fee_denominator' / Int64ul,
    'pnl_numerator' / Int64ul,
    'pnl_denominator' / Int64ul,
    'swap_fee_numerator' / Int64ul,
    'swap_fee_denominator' / Int64ul,
    # OutPutData
    'base_need_take_pnl' / Int64ul,
    'quote_need_take_pnl' / Int64ul,
    'quote_total_pnl' / Int64ul,
    'base_total_pnl' / Int64ul,
    # 128
    'quote_total_deposited' / BytesInteger(16, signed=False, swapped=True),
    'base_total_deposited' / BytesInteger(16, signed=False, swapped=True),
    'swap_base_in_amount' / BytesInteger(16, signed=False, swapped=True),
    'swap_quote_out_amount' / BytesInteger(16, signed=False, swapped=True),

    'swap_base2_quote_fee' / Int64ul,
    # 128
    'swap_quote_in_amount' / BytesInteger(16, signed=False, swapped=True),
    'swap_base_out_amount' / BytesInteger(16, signed=False, swapped=True),

    'swap_quote2_base_fee' / Int64ul,
    # AMM Vault
    'base_vault' / Bytes(32),
    'quote_vault' / Bytes(32),
    # Mint
    'base_mint' / Bytes(32),
    'quote_mint' / Bytes(32),
    'lp_mint' / Bytes(32),
    # Market
    'open_orders' / Bytes(32),
    'market_id' / Bytes(32),
    'serum_program_id' / Bytes(32),
    'target_orders' / Bytes(32),
    'withdraw_queue' / Bytes(32),
    'lp_vault' / Bytes(32),
    'amm_owner' / Bytes(32),

    'lpReserve' / Int64ul,
)

SPL_MINT_LAYOUT = cStruct(
    'mintAuthorityOption' / Int32ul,
    'mintAuthority' / Bytes(32),
    'supply' / Int64ul,
    'decimals' / Int8ul,
    'isInitialized' / Int8ul,
    'freezeAuthorityOption' / Int32ul,
    'freezeAuthority' / Bytes(32),
)

MARKET_STATE_LAYOUT_V3 = cStruct(
    'ownAddress' / Bytes(32),
    'vaultSignerNonce' / Int8ul,
    'baseMint' / Bytes(32),
    'quoteMint' / Bytes(32),
    'baseVault' / Bytes(32),
    'baseDepositsTotal' / Int64ul,
    'baseFeesAccrued' / Int64ul,
    'quoteVault' / Bytes(32),
    'quoteDepositsTotal' / Int64ul,
    'quoteFeesAccrued' / Int64ul,
    'quoteDustThreshold' / Int64ul,
    'requestQueue' / Bytes(32),
    'eventQueue' / Bytes(32),
    'bids' / Bytes(32),
    'asks' / Bytes(32),
    'baseLotSize' / Int64ul,
    'quoteLotSize' / Int64ul,
    'feeRateBps' / Int64ul,
    'referrerRebatesAccrued' / Int64ul,
)

PoolInfoLayout = cStruct(
    'bump' / Int8ul,
    'ammConfig' / Bytes(32),
    'creator' / Bytes(32),
    'mintA' / Bytes(32),
    'mintB' / Bytes(32),
    'vaultA' / Bytes(32),
    'vaultB' / Bytes(32),
    'observationId' / Bytes(32),
    'mintDecimalsA' / Int8ul,
    'mintDecimalsB' / Int8ul,
    'tickSpacing' / Int16ul,
    'liquidity' / BytesInteger(16, signed=False, swapped=True),
    'sqrtPriceX64' / BytesInteger(16, signed=False, swapped=True),
    'observationIndex' / Int16ul,
    'observationUpdateDuration' / Int16ul,
    'feeGrowthGlobalX64A' / BytesInteger(16, signed=False, swapped=True),
    'feeGrowthGlobalX64B' / BytesInteger(16, signed=False, swapped=True),
    'protocolFeesTokenA' / Int64ul,
    'protocolFeesTokenB' / Int64ul,
    'swapInAmountTokenA' / BytesInteger(16, signed=False, swapped=True),
    'swapOutAmountTokenB' / BytesInteger(16, signed=False, swapped=True),
    'swapInAmountTokenB' / BytesInteger(16, signed=False, swapped=True),
    'swapOutAmountTokenA' / BytesInteger(16, signed=False, swapped=True),
    'status' / Int8ul,
    'totalFeesTokenA' / Int64ul,
    'totalFeesClaimedTokenA' / Int64ul,
    'totalFeesTokenB' / Int64ul,
    'totalFeesClaimedTokenB' / Int64ul,
    'fundFeesTokenA' / Int64ul,
    'fundFeesTokenB' / Int64ul,
    'startTime' / Int64ul,
) 