[root@linuxserver pytontest]# find py-files/ -type f -print0 | xargs -r0 grep -F 'hsutils'
py-files/lsof_file_is_open.py:import hsutils
py-files/lsof_file_is_open.py:        results = hsutils.run_cmd(cmd)
py-files/mli_us_EOD.py:import hsutils
py-files/mli_us_EOD.py:      mailObject = hsutils.HeliosEmail()
py-files/mli_us_EOD.py:  list_of_tuples = hsutils.db_conn.queryDatabase(db_connection, sql_to_use)
py-files/newedge_et_EOD.py:import hsutils
py-files/newedge_et_EOD.py:        results = hsutils.run_cmd( command_to_use )
py-files/newedge_et_EOD.py:            results = hsutils.run_cmd( command_to_use )
py-files/newedge_et_EOD.py:   list_of_results = hsutils.db_utils.getSimpleListFromDB( sql_to_use, db_connection )
py-files/nomura.py:import hsutils
py-files/nomura.py:    connection_string = hsutils.db_conn.getSystemConnectionString ( 'AS' )
py-files/nomura.py:    db_connection = hsutils.db_conn.getDatabaseConnection ( connection_string )
py-files/nomura.py:    file_date = hsutils.db_utils.getSimpleListFromDB( sql_to_use, db_connection )
py-files/nomura.py:        connection_string = hsutils.db_conn.getSystemConnectionString ( 'AS' )
py-files/nomura.py:        db_connection = hsutils.db_conn.getDatabaseConnection ( connection_string )
py-files/nomura.py:        rows = hsutils.queryDatabase( db_connection, sql_to_use )
py-files/nomura.py:        results = hsutils.run_cmd ( command )
py-files/nomura.py:        connection_string = hsutils.db_conn.getSystemConnectionString ( 'AS' )
py-files/nomura.py:        db_connection = hsutils.db_conn.getDatabaseConnection ( connection_string )
py-files/nomura.py:        rows = hsutils.queryDatabase( db_connection, sql_to_use )
py-files/nomura.py:                query_set = hsutils.PostgresDAO.QuerySet(
py-files/nomura.py:        self._connection = hsutils.PostgresDAO.DAO_BusinessUnitCode( 'AS', read_only = False )
py-files/nova_patch_SH_services.py:import hsutils
py-files/nova_patch_SH_services.py:    results = hsutils.run_cmd(cmd_to_patch,60)
py-files/nova_patch_SH_services.py:        results = hsutils.run_cmd(cmd_to_patch,60)
py-files/nova_patch_SH_services.py:        results = hsutils.run_cmd(cmd_to_push,180)
py-files/nova_patch_SH_services.py:            results = hsutils.run_cmd(cmd_to_push,180)
py-files/nova_patch_SH_services.py:    log = hsutils.create_log(name = __name__, verbose = args.verbose)
py-files/om_rebalancer.py:import hsutils
py-files/om_rebalancer.py:    configured_exchanges_list = hsutils.getSimpleListFromDB( "SELECT DISTINCT short_name FROM symbol_type_exchange_mapping;", self.db_connection )
py-files/om_rebalancer.py:      sql_fh.write("DELETE FROM om_keys WHERE symbol in (" + hsutils.quotedStrings(inactive_symbols_list) + ");\n")
py-files/om_rebalancer.py:  results = hsutils.run_cmd("scp " + q_script + " helios@kdb3:" + q_script)
py-files/om_rebalancer.py:    results = hsutils.run_cmd("ssh helios@kdb3 q " + q_script)
py-files/om_rebalancer.py:      results = hsutils.run_cmd("scp helios@kdb3:/tmp/" + out_name + ".csv /tmp")
py-files/om_rebalancer.py:  return hsutils.getSimpleListFromDB( SQL_to_use, db_connection )
py-files/om_rebalancer.py:  om_keys_tuple_list = hsutils.queryDatabase(db_connection, SQL_to_use)
py-files/om_rebalancer.py:  return hsutils.getSimpleListFromDB( SQL_to_use, db_connection )
py-files/om_rebalancer.py:  return hsutils.getSimpleListFromDB( SQL_to_use, db_connection )
py-files/om_rebalancer.py:  return hsutils.getSimpleListFromDB( SQL_to_use, db_connection )
py-files/om_rebalancer.py:  list_of_tuples = hsutils.queryDatabase(db_connection, SQL_to_use)
py-files/om_rebalancer.py:    results = hsutils.run_cmd(novagenUpdateCommand,600)
py-files/om_rebalancer.py:      results = hsutils.run_cmd(novagenUpdateCommand,1200)
py-files/om_rebalancer.py:      results = hsutils.run_cmd(novagenUpdateCommand,1200)
py-files/om_rebalancer.py:        results = hsutils.run_cmd(novagenUpdateCommand,1200)
py-files/om_rebalancer.py:    results = hsutils.run_cmd(novagenUpdateCommand,1200)
py-files/om_rebalancer.py:  novagen_db_connection = hsutils.getDatabaseConnection(hsutils.getNovagenROConnectionString( business_unit_code ))
py-files/om_rebalancer.py:  multi_exchange_om_pool_tuples_list = hsutils.queryDatabase(novagen_db_connection, multi_exch_om_sql);
py-files/om_rebalancer.py:  single_exchange_om_pool_tuples_list = hsutils.queryDatabase(novagen_db_connection, single_exch_om_sql);
py-files/om_rebalancer.py:                    choices = hsutils.get_valid_business_unit_codes(),
py-files/om_rebalancer.py:connection_string = hsutils.getSystemConnectionString( bus_unit_code )
py-files/om_rebalancer.py:db_connection = hsutils.getDatabaseConnection(connection_string)
py-files/option_brussels_log_processor.py:import hsutils
py-files/option_brussels_log_processor.py:    email=hsutils.SupportEmail( business_unit_code )
py-files/option_brussels_log_processor.py:logger=hsutils.create_log('main')
py-files/option_brussels_log_processor.py:# the hsutils logging module to support this natively;  as it is I'm using
py-files/or_symbol_updater.py:import hsutils
py-files/or_symbol_updater.py:      email = hsutils.HeliosEmail()
py-files/order_life_cycle.py:import hsutils
py-files/order_life_cycle.py:                        choices=hsutils.get_valid_business_unit_codes(), 
py-files/order_life_cycle.py:logger = hsutils.create_log( 'main', verbose )
py-files/OrderLoggerDataObject.py:import hsutils
py-files/OrderLoggerDataObject.py:    hsutils.verify_ssh_trusted_host(business_unit_code)    
py-files/OrderLoggerDataObject.py:    __run_control = hsutils.ParallelRunner(command_specs=__command_list, results=__results, verbose=False, max_thread_time=60, thread_count=10)
py-files/parse_asx_drop_csv.py:import hsutils
py-files/parse_venue_fills.py:import hsutils
py-files/parse_venue_fills.py:        hsutils.debug( log_fh, "Operations complete for exec_id: " + self._exec_id )
py-files/parse_venue_fills.py:    db_connection = hsutils.getDatabaseConnection(deployment_connection_string)
py-files/parse_venue_fills.py:    hsutils.debug( log_fh, sql )
py-files/parse_venue_fills.py:    venue_details = hsutils.queryDatabase(db_connection, sql, "true")
py-files/parse_venue_fills.py:           hsutils.debug( log_fh, key + " = " + str(venue_details_dict[key]) )
py-files/parse_venue_fills.py:    hsutils.debug( log_fh, "Getting source files of format " + src_file )
py-files/parse_venue_fills.py:    hsutils.debug( log_fh, "Got file: " + src_file )
py-files/parse_venue_fills.py:    file_transfer_object = hsutils.FileTransferObject( src_dir, src_file, dst_dir, dst_file)
py-files/parse_venue_fills.py:    sftp_connection = hsutils.SFTPConnection( host, port, user, password, ssh_key )
py-files/parse_venue_fills.py:    files = hsutils.pgpDecryptFiles( files_list, decrypt_key, False )
py-files/parse_venue_fills.py:        hsutils.debug( log_fh, "Retrieved file: " + fname )
py-files/parse_venue_fills.py:    hsutils.debug( log_fh, "Executing SQL to get DB execs:\n" + sql )
py-files/parse_venue_fills.py:    sys_conn_string = hsutils.getSystemConnectionString(args.business_unit_code)
py-files/parse_venue_fills.py:    db_conn = hsutils.getDatabaseConnection(sys_conn_string)
py-files/parse_venue_fills.py:    exec_ids = hsutils.getSimpleListFromDB(sql, db_conn)
py-files/parse_venue_fills.py:    hsutils.debug( log_fh, "List of exec IDs for logical exchange " + logical_exchange + " as below:" )
py-files/parse_venue_fills.py:        hsutils.debug( log_fh, eid )
py-files/parse_venue_fills.py:        hsutils.debug( log_fh, "Parsing file: " + file_name )
py-files/parse_venue_fills.py:                   hsutils.debug( log_fh, "Performing assignment: " + assign_member_value )
py-files/parse_venue_fills.py:                      #hsutils.run_cmd( assign_member_value, timeout=3 )
py-files/parse_venue_fills.py:                         hsutils.debug(log_fh, assign_member_value + " failed.")
py-files/parse_venue_fills.py:                     hsutils.debug( hsinsert_log_fh, trade_obj._hsinsert )
py-files/parse_venue_fills.py:                     hsutils.debug( sql_log_fh, trade_obj._insert_sql )
py-files/parse_venue_fills.py:                 choices=hsutils.get_valid_business_unit_codes(),
py-files/pbm_log_parser_gen.py:import hsutils
py-files/pbm_log_parser_gen.py:      choices = hsutils.db_conn.get_valid_business_unit_codes(),
py-files/pbm_monitor.py:import hsutils
py-files/pbm_monitor.py:      choices = hsutils.db_conn.get_valid_business_unit_codes(),
py-files/pcap_log_collection.py:import hsutils
py-files/pcap_log_collection.py:                          choices = hsutils.get_valid_business_unit_codes(),
py-files/pcap_log_collection.py:    #db_conn = hsutils.getDatabaseConnection( hsutils.getSystemConnectionString( bu ) )
py-files/populate_cfe_future_settlement_prices_from_md.py:import hsutils
py-files/populate_cfe_future_settlement_prices_from_md.py:    log = hsutils.create_log(name = __name__, verbose = args.verbose)
py-files/populate_system_info_from_cobs.py:import hsutils
py-files/populate_system_info_from_cobs.py:   parser.add_argument('-L',dest='business_unit_code',choices=hsutils.get_valid_business_unit_codes(),help='Business Unit Code',required=True)
py-files/populate_system_info_from_cobs.py:   cobsdb=hsutils.getDatabaseConnection('host=cobsdb1 dbname=helios user=helios')
py-files/populate_system_info_from_cobs.py:   db = hsutils.getDatabaseConnection(hsutils.getSystemConnectionString(args.business_unit_code))
py-files/prep_host.py:import hsutils
py-files/prep_host.py:    nova_cmd_ret = hsutils.run_cmd(nova_cmd)
py-files/prep_host.py:        ret = hsutils.run_cmd(scp_cmd, 60)
py-files/prep_host.py:        ret = hsutils.run_cmd(scp_cmd, 3000)
py-files/prep_host.py:    ret = hsutils.run_cmd(scp_cmd, 300)
py-files/prep_host.py:    ret = hsutils.run_cmd(ssh_cmd, 600)
py-files/prep_host.py:    ret = hsutils.run_cmd(ssh_cmd, 30)
py-files/prep_host.py:    ret = hsutils.run_cmd(cronbuilder_cmd, 90)
py-files/prep_host.py:        ret = hsutils.run_cmd(cmd, 90)
py-files/prep_host.py:        ret = hsutils.run_cmd(cmd, 10)
py-files/prep_host.py:    ret = hsutils.run_cmd(puppet_cmd, timeout=600)
py-files/prep_host.py:    log = hsutils.create_log(name = __name__, verbose = args.verbose)
py-files/prep_host.py:    ret = hsutils.run_cmd(push_to_deployment_sync_cmd, 90)
py-files/process_db_applies.py:import hsutils
py-files/process_db_applies.py:    email = hsutils.HeliosEmail()
py-files/process_EOD.py:import hsutils
py-files/process_EOD.py:  query_list = hsutils.db_utils.getSimpleListFromDB( SQL_to_use, db_connection )
py-files/process_EOD.py:  symbols_tuple_list = hsutils.db_conn.queryDatabase( db_connection, SQL_TO_USE )
py-files/process_EOD.py:  hsutils.run_cmd("ssh " + target_host + " \"mkdir -p " + target_dir + "\"")
py-files/process_EOD.py:  results = hsutils.run_cmd(command)
py-files/process_EOD.py:  results = hsutils.run_cmd(command)
py-files/process_EOD.py:  hsutils.run_cmd( command )
py-files/process_EOD.py:  results = hsutils.run_cmd( command )
py-files/process_EOD.py:                    choices = hsutils.db_conn.get_valid_business_unit_codes(),
py-files/process_EOD.py:connection_string = hsutils.db_conn.getSystemConnectionString( bus_unit_code )
py-files/process_EOD.py:db_connection = hsutils.db_conn.getDatabaseConnection( connection_string )
py-files/push.py:import hsutils
py-files/push.py:    bucs_string = hsutils.quotedStrings(result)
py-files/push_hftmm.py:import hsutils
py-files/push_hftmm.py:            remote_run = hsutils.run_cmd(cmd)
py-files/push_to_deployment.py:import hsutils
py-files/push_to_deployment.py:    log = hsutils.create_log(name = __name__, verbose = args.verbose)
py-files/python_document_generator.py:import hsutils
py-files/python_document_generator.py:    results = hsutils.run_cmd(cmd)
py-files/python_document_generator.py:        results = hsutils.run_cmd(cmd)
py-files/python_document_generator.py:    hsutils.run_cmd(cmd)
py-files/python_document_generator.py:    results = hsutils.run_cmd(cmd)
py-files/ref_trader_migration_tool.py:import hsutils
py-files/ref_trader_migration_tool.py:                     choices = hsutils.db_conn.get_valid_business_unit_codes(),
py-files/ref_trader_migration_tool.py:    db_conn_data = hsutils.db_conn.getSystemConnectionDict(args.business_unit_code)
py-files/reinit_compliance_for_locates.py:import hsutils
py-files/reinit_compliance_for_locates.py:        self.__locates_symbol_time_dicts_list = hsutils.queryDatabase(db_conn, sql, "true")
py-files/reinit_compliance_for_locates.py:           self.__symbol_buckets_exact_list = hsutils.queryDatabase(db_conn, sql, "true")
py-files/reinit_compliance_for_locates.py:           self.__symbol_buckets_regexp_list = hsutils.queryDatabase(db_conn, sql, "true")
py-files/reinit_compliance_for_locates.py:               ret = hsutils.run_cmd(cmd)
py-files/reinit_compliance_for_locates.py:                 hsutils.run_cmd(alert_cmd)
py-files/reinit_compliance_for_locates.py:        self.__last_reinitialized_time = hsutils.getSimpleListFromDB(sql, db_conn)
py-files/reinit_compliance_for_locates.py:                 choices=hsutils.get_valid_business_unit_codes(),
py-files/reinit_compliance_for_locates.py:sys_conn_string = hsutils.getSystemConnectionString(args.business_unit_code)
py-files/reinit_compliance_for_locates.py:db_conn = hsutils.getDatabaseConnection(sys_conn_string)
py-files/remote_sql_file_apply.py:import hsutils
py-files/remote_sql_file_apply.py:                   choices = hsutils.db_conn.get_valid_business_unit_codes(),
py-files/remote_sql_file_apply.py:mail = hsutils.HeliosEmail()
py-files/remote_sql_file_apply.py:    ssh = hsutils.RemoteFileReader(args.remote_host)
py-files/remove_initiator.py:import hsutils
py-files/remove_initiator.py:  return hsutils.db_utils.getSimpleListFromDB(search_SQL, db_connection)
py-files/remove_initiator.py:  sequence_number = hsutils.db_utils.getSimpleListFromDB(sql_to_use, db_connection)[0]
py-files/remove_initiator.py:  list_of_tuples = hsutils.db_conn.queryDatabase(db_connection, sqlToUse)
py-files/remove_initiator.py:                    choices = hsutils.db_conn.get_valid_business_unit_codes(),
py-files/remove_initiator.py:sys_connection_string = hsutils.db_conn.getSystemConnectionString( bus_unit_code )
py-files/remove_initiator.py:db_connection = hsutils.db_conn.getDatabaseConnection(sys_connection_string)
py-files/remove_initiator.py:initiatorsString = hsutils.quotedStrings(initiators_list)
py-files/remove_symbols_from_system.py:import hsutils
py-files/remove_symbols_from_system.py:sys_connection_string = hsutils.getSystemConnectionString( bus_unit_name )
py-files/retire_host.py:import hsutils
py-files/retire_host.py:    Wrapper around hsutils.run_cmd, with extra conditional logic. It runs
py-files/retire_host.py:    results = hsutils.run_cmd(cmd_string)
py-files/retire_host.py:AND    host = '%s';""" % (hsutils.quotedStrings(ok_to_disable_cmds), host)
py-files/retire_host.py:AND    cmd IN (%s);""" % (host, hsutils.quotedStrings(ok_to_disable_cmds))
py-files/retire_host.py:    log = hsutils.create_log(verbose = args.verbose)
py-files/retire_host.py:    ret = hsutils.run_cmd(push_to_deployment_sync_cmd, 90)
py-files/run_feeddump_check.py:import hsutils
py-files/run_feeddump_check.py:    log = hsutils.create_log("FeedDump_"+book_interface)
py-files/run_feeddump_check.py:        results = hsutils.run_cmd(cmd)
py-files/run_feeddump_check.py:        mailObject = hsutils.HeliosEmail()
py-files/run_feeddump_check.py:        hsutils.run_cmd(cmd_alert)
py-files/run_feeddump_sip_feeds.py:import hsutils
py-files/run_feeddump_sip_feeds.py:    log = hsutils.create_log("FeedDumpHeliosNbboSlow")
py-files/run_feeddump_sip_feeds.py:        results = hsutils.run_cmd(cmd)
py-files/run_feeddump_sip_feeds.py:        mailObject = hsutils.HeliosEmail()
py-files/run_feeddump_sip_feeds.py:        hsutils.run_cmd(cmd_alert)
py-files/sbi.py:import hsutils
py-files/sbi.py:        connection_string = hsutils.db_conn.getSystemConnectionString ( 'AS' )
py-files/sbi.py:        db_connection = hsutils.db_conn.getDatabaseConnection ( connection_string )
py-files/sbi.py:        active_symbols = hsutils.db_utils.getSimpleListFromDB( sql_to_use, db_connection )
py-files/scream_if_celoxica_book_looks_hosed.py:import hsutils
py-files/scream_if_celoxica_book_looks_hosed.py:    email = hsutils.HeliosEmail()
py-files/st_slippage_eod.py:import hsutils
py-files/st_slippage_eod.py:    email=hsutils.HeliosEmail()
py-files/strategy_tools.py:import hsutils
py-files/swap_cs_interfaces.py:import hsutils
py-files/swap_cs_interfaces.py:  query_list = hsutils.db_utils.getSimpleListFromDB( sql_to_use, db_connection )
py-files/swap_cs_interfaces.py:  query_list = hsutils.db_utils.getSimpleListFromDB( sql_to_use, db_connection )
py-files/swap_cs_interfaces.py:  query_list = hsutils.db_utils.getSimpleListFromDB( sql_to_use, db_connection )
py-files/swap_cs_interfaces.py:  gen_tko_interface_info = hsutils.db_conn.queryDatabase(db_connection, sql_to_use)[0]
py-files/swap_cs_interfaces.py:  tko_interface_info = hsutils.db_conn.queryDatabase(db_connection, sql_to_use)[0]
py-files/swap_cs_interfaces.py:  helios_interface_info = hsutils.db_conn.queryDatabase(db_connection, sql_to_use)[0]
py-files/swap_cs_interfaces.py:  helios_sniper_service_id = hsutils.db_utils.getSimpleListFromDB( sql_to_use, db_connection )
py-files/swap_cs_interfaces.py:  return_value = hsutils.db_utils.getSimpleListFromDB(sql_to_use, db_connection)[0]
py-files/swap_cs_interfaces.py:  list_of_service_ids = hsutils.db_utils.getSimpleListFromDB(sql_to_use, db_connection)
py-files/swap_cs_interfaces.py:connection_string = hsutils.db_conn.getSystemConnectionString( 'US' )
py-files/swap_cs_interfaces.py:db_connection = hsutils.db_conn.getDatabaseConnection( connection_string )
py-files/sync_block_hedge_tables.py:import hsutils
py-files/sync_block_hedge_tables.py:# Wrapper around hsutils.transact_queries that checks for -v (verbose),
py-files/sync_block_hedge_tables.py:   db = hsutils.TransactionalDB(**creds_dict)
py-files/tko_OI_usage.py:import hsutils
py-files/tko_OI_usage.py:                     choices = hsutils.db_conn.get_valid_business_unit_codes(),
py-files/tko_OI_usage.py:    db_conn_data = hsutils.db_conn.getSystemConnectionDict(args.business_unit_code)
py-files/tko_OI_usage.py:    db_conn = hsutils.db_conn.TransactionalDB(host = db_conn_data['host'],
py-files/tko_taskset.py:import hsutils
py-files/tko_taskset.py:import hsutils
py-files/tko_taskset.py:    """ %( hsutils.quotedStrings(tko_trader_cmds) )
py-files/tko_taskset.py:                     choices = hsutils.db_conn.get_valid_business_unit_codes(),
py-files/tko_taskset.py:    log = hsutils.create_log(name = __name__, verbose = args.verbose)
py-files/trader_authorization_report.py:import hsutils
py-files/transfer_auction_offsetting_positions.py:import hsutils
py-files/transfer_auction_offsetting_positions.py:    results = hsutils.run_cmd(current_sell_insert)
py-files/transfer_auction_offsetting_positions.py:    results = hsutils.run_cmd(current_buy_insert)
py-files/transfer_drop_trades.py:import hsutils
py-files/transfer_drop_trades.py:hsutils.verify_ssh_trusted_host(business_unit_code)
py-files/transfer_PBM_positions.py:import hsutils
py-files/transfer_PBM_positions.py:    results = hsutils.run_cmd(current_insert)
py-files/transfer_PBM_positions.py:    results = hsutils.run_cmd(current_insert)
py-files/transfer_PBM_positions.py:    email_to_address = hsutils.SupportEmail( business_unit_code ).to_addrs
py-files/update_all_exposure_groups.py:import hsutils
py-files/update_all_exposure_groups.py:        self.__group_names = hsutils.getSimpleListFromDB(sql, db_conn)
py-files/update_all_exposure_groups.py:        results = hsutils.run_cmd(cmd)
py-files/update_all_exposure_groups.py:                 choices=hsutils.get_valid_business_unit_codes(),
py-files/update_all_exposure_groups.py:sys_conn_string = hsutils.getSystemConnectionString(args.business_unit_code)
py-files/update_all_exposure_groups.py:prod_conn_info  = hsutils.getSystemConnectionDict(args.business_unit_code, 'system')
py-files/update_all_exposure_groups.py:drop_conn_info  = hsutils.getSystemConnectionDict(args.business_unit_code, 'drop')
py-files/update_all_exposure_groups.py:db_conn = hsutils.getDatabaseConnection(sys_conn_string)
py-files/update_covariance_matrix_daily.py:import hsutils
py-files/update_covariance_matrix_daily.py:    db_interface = hsutils.TransactionalDB(host=db_host, db=db_name, user=db_user)
py-files/update_covariance_matrix_daily.py:    db_interface = hsutils.TransactionalDB(host=db_host, db=db_name, user=db_user)
py-files/update_covariance_matrix_daily.py:email=hsutils.HeliosEmail()
py-files/update_research_host.py:import hsutils
py-files/update_research_host.py:    host_info = hsutils.get_host_info(host)
py-files/update_research_host.py:    build_host = hsutils.get_build_host(distribution, 'core2', research_label)
py-files/update_research_host.py:    pull_results = hsutils.run_cmd(pull_cmd, 600)
py-files/update_research_host.py:    push_results = hsutils.run_cmd(push_cmd, 1800)
py-files/update_research_host.py:        bounce_results = hsutils.run_cmd(bounce_cmd, 60)
py-files/upgrade_release.py:    This subroutine is copied from hsutils due to the fact that hsutils may
py-files/upgrade_release.py:    This subroutine is copied from hsutils due to the fact that hsutils may
py-files/upgrade_release.py:        This subroutine is copied from hsutils due to the fact that hsutils may
py-files/upload_abn_order_logs.py:import hsutils
py-files/upload_abn_order_logs.py:    connection_string = hsutils.db_conn.getSystemConnectionString ( business_unit )
py-files/upload_abn_order_logs.py:    db_connection = hsutils.db_conn.getDatabaseConnection ( connection_string )
py-files/upload_abn_order_logs.py:    order_interfaces = hsutils.db_utils.getSimpleListFromDB( sql_to_use, db_connection )
py-files/upload_abn_order_logs.py:                        choices=hsutils.get_valid_business_unit_codes(),
py-files/us_upd_order_monitor_configs.py:import hsutils
py-files/us_upd_order_monitor_configs.py:                    choices = hsutils.get_valid_business_unit_codes(),
py-files/us_upd_order_monitor_configs.py:sys_connection_string = hsutils.getSystemConnectionString( bus_unit_code )
py-files/us_upd_order_monitor_configs.py:db_connection = hsutils.getDatabaseConnection(sys_connection_string)
py-files/vix_future_roll_TKOHFTMM_update.py:import hsutils
py-files/vix_future_roll_TKOHFTMM_update.py:    term_strings = hsutils.quotedStrings(next_nine_vix.values())
py-files/vix_future_roll_TKOHFTMM_update.py:AND    active;""" %(hsutils.quotedStrings(symbol_list))
py-files/vix_future_roll_TKOHFTMM_update.py:    """ %(hsutils.quotedStrings(booking_initiators))
py-files/vix_future_roll_TKOHFTMM_update.py:        """ % (hsutils.quotedStrings(booking_initiator), front_index, offset)
py-files/vix_future_roll_TKOHFTMM_update.py:    log = hsutils.create_log(verbose = args.verbose)
py-files/gather_debug (2).py:import hsutils
py-files/gather_debug (2).py:        email = hsutils.HeliosEmail()
py-files/gather_debug (2).py:        result = hsutils.run_cmd(cmd)
py-files/gather_debug (2).py:        result = hsutils.run_cmd(grep_test_cmd, 3)
py-files/gather_debug (2).py:        result = hsutils.run_cmd(grep_research_cmd, 3)
py-files/gather_debug (2).py:        result = hsutils.run_cmd(grep_path, 3)
py-files/gather_debug (2).py:    result = hsutils.run_cmd(cmd)
py-files/gather_debug (2).py:    result = hsutils.run_cmd(ls_symlink)
py-files/gather_debug (2).py:    result = hsutils.run_cmd(file_cmd, 3)
py-files/gather_debug (2).py:    result = hsutils.run_cmd(cmd, 3)
py-files/gather_debug (2).py:    result = hsutils.run_cmd(cmd, 20)
py-files/gather_debug (2).py:    result = hsutils.run_cmd(gstack_cmd, 120)
py-files/gather_debug (2).py:    result = hsutils.run_cmd(lsof_cmd, 5)
py-files/gather_debug (2).py:    result = hsutils.run_cmd(top_cmd, 3)
py-files/gather_debug (2).py:    result = hsutils.run_cmd(top_cmd, 3)
py-files/gather_debug (2).py:    result = hsutils.run_cmd(ps_cmd, 3)
py-files/gather_debug (2).py:    result = hsutils.run_cmd(netstat_cmd, 5)
py-files/gather_debug (2).py:    result = hsutils.run_cmd(strace_cmd, 10)
py-files/gather_debug (2).py:    result = hsutils.run_cmd(bt_cmd, 60)
py-files/gen_icarus_params_on_strat_csv (2).py:import hsutils
py-files/gen_icarus_params_on_strat_csv (2).py:    results = hsutils.run_cmd("scp " + csvfile + " " + destination)
py-files/gen_icarus_params_on_strat_csv (2).py:    log = hsutils.create_log("GenIcarusParamRisk")
py-files/get_ftp_locates (2).py:import hsutils
py-files/get_ftp_locates (2).py:        connection_string = hsutils.db_conn.getSystemConnectionString ( bu )
py-files/get_ftp_locates (2).py:        db_connection = hsutils.db_conn.getDatabaseConnection ( connection_string )
py-files/get_ftp_locates (2).py:        file_date = hsutils.db_utils.getSimpleListFromDB( sql_to_use, db_connection )
py-files/grey_team_access_auditor (2).py:import hsutils
py-files/grey_team_access_auditor (2).py:    mail=hsutils.HeliosEmail()
py-files/grey_team_access_auditor (2).py:mail=hsutils.HeliosEmail()
py-files/hftmm_symbol_balancer (2).py:import hsutils
py-files/hftmm_symbol_balancer (2).py:                     choices = hsutils.db_conn.get_valid_business_unit_codes(),
py-files/host_taskset (2).py:import hsutils
py-files/host_taskset (2).py:        choices=hsutils.db_conn.get_valid_business_unit_codes(),
py-files/host_taskset (2).py:    log = hsutils.create_log(name=__name__, verbose=args.verbose)
py-files/hs_taskpool (2).py:### was taken from the rjones ThreadPool implementation in hsutils.py
py-files/hsutils (2).py:# hsutils.py has gone through a namespace layout restructure where various
py-files/hsutils (2).py:# functions/classes through the global namespace of hsutils, the following
py-files/hsutils (2).py:       email.attach_text_file('hsutils.py')
py-files/hsutils (2).py:    sys.exit("\nERROR: invalid parameter to hsutils.getCgroup(int).  Input not of type int.")
py-files/hsutils (2).py:    sys.exit("\nERROR: invalid parameter to hsutils.setCgroupToRoot(int).  Input not of type int.")
py-files/import_futures_product_group_mappings (2).py:import hsutils
py-files/import_futures_product_group_mappings (2).py:                 choices=hsutils.get_valid_business_unit_codes(),
py-files/import_futures_product_group_mappings (2).py:log = hsutils.create_log(name = __name__)
py-files/importLivVolFills (2).py:import hsutils
py-files/importLivVolFills (2).py:   exec_id_list = hsutils.getSimpleListFromDB(exec_id_sql, db)
py-files/importLivVolFills (2).py:   file_transfer_object = hsutils.FileTransferObject( src_dir, src_file, dst_dir, dst_file)
py-files/importLivVolFills (2).py:   sftp_connection = hsutils.SFTPConnection(host,port,user_name,passwd,'')
py-files/importLivVolFills (2).py:	symbol = hsutils.db_utils.getSimpleListFromDB( sql, db )[0]
py-files/importLivVolFills (2).py:	symbol = hsutils.db_utils.getSimpleListFromDB( sql, db )[0]
py-files/importLivVolFills (2).py:   initiator  = hsutils.db_utils.getSimpleListFromDB( sql, db )[0]
py-files/importLivVolFills (2).py:   parser.add_argument('-L',dest = 'business_unit_code',choices=hsutils.get_valid_business_unit_codes(),help='Business Unit Code',required =True)
py-files/importLivVolFills (2).py:   db =  hsutils.getDatabaseConnection(hsutils.getSystemConnectionString(business_unit_code))
py-files/init_mgr_TKO_Auction (2).py:import hsutils
py-files/init_mgr_TKO_Auction (2).py:                    choices = hsutils.db_conn.get_valid_business_unit_codes(),
py-files/init_mgr_TKO_BetaHedger (2).py:import hsutils
py-files/init_mgr_TKO_BetaHedger (2).py:                    choices = hsutils.db_conn.get_valid_business_unit_codes(),
py-files/init_mgr_TKO_BRU (2).py:import hsutils
py-files/init_mgr_TKO_BRU (2).py:                     choices = hsutils.db_conn.get_valid_business_unit_codes(),
py-files/init_mgr_TKO_BRU (2).py:    db_conn_data = hsutils.db_conn.getSystemConnectionDict(args.business_unit_code)
py-files/init_mgr_TKO_BRU (2).py:    #db_conn = hsutils.db_conn.TransactionalDB(host = 'arymarczuk1',
py-files/init_mgr_TKO_BRU (2).py:    db_conn = hsutils.db_conn.TransactionalDB(host = db_conn_data['host'],
py-files/init_mgr_TKO_HFTMM (2).py:import hsutils
py-files/init_mgr_TKO_HFTMM (2).py:        choices = hsutils.db_conn.get_valid_business_unit_codes(),
py-files/init_mgr_TKO_HFTMM (2).py:    db_conn_data = hsutils.db_conn.getSystemConnectionDict(args.business_unit_code)
py-files/init_mgr_TKO_REMOVE (2).py:import hsutils
py-files/init_mgr_TKO_REMOVE (2).py:                     choices = hsutils.db_conn.get_valid_business_unit_codes(),
py-files/init_mgr_TKO_REMOVE (2).py:    db_conn_data = hsutils.db_conn.getSystemConnectionDict(args.business_unit_code)
py-files/init_mgr_TKO_REMOVE (2).py:    db_conn = hsutils.db_conn.TransactionalDB(host = db_conn_data['host'],
py-files/init_mgr_TKO_REMOVE (2).py:    #db_conn = hsutils.db_conn.TransactionalDB(host = 'sdonadio',
py-files/init_mgr_TKO_REMOVE (2).py:    #db_conn = hsutils.db_conn.TransactionalDB(host = 'heliosdb1',
py-files/initiator_param_auditor (2).py:import hsutils
py-files/initiator_param_auditor (2).py:db=hsutils.TransactionalDB(host=dbhost, user=dbuser, db=dbname)
py-files/investigate_auctions_data_problems (2).py:import hsutils
py-files/investigate_auctions_data_problems (2).py:    choices = hsutils.db_conn.get_valid_business_unit_codes()
py-files/investigate_auctions_data_problems (2).py:    db_conn_data = hsutils.db_conn.getSystemConnectionDict(args.business_unit_code)
py-files/investigate_auctions_data_problems (2).py:    db_conn = hsutils.db_conn.TransactionalDB(host = db_conn_data['host'],
py-files/logtail_consumer_config (2).py:import sunshared.hsutils
py-files/lsof_file_is_open (2).py:import hsutils
py-files/lsof_file_is_open (2).py:        results = hsutils.run_cmd(cmd)
py-files/manage_stat_arb_symbols (2).py:import hsutils
py-files/manage_stat_arb_symbols (2).py:    hsutils.debug( log_fh, "Retrieved the following params file info ...\n" )
py-files/manage_stat_arb_symbols (2).py:            hsutils.debug( log_fh, str( key ) + ": " + str( list_elem[ key ] ) + "\n" )
py-files/manage_stat_arb_symbols (2).py:    # Create object of class hsutils.SFTPConnection.
py-files/manage_stat_arb_symbols (2).py:    sftp_connection = hsutils.SFTPConnection( file_info_dict[ 'host' ], \
py-files/manage_stat_arb_symbols (2).py:    file_transfer_object = hsutils.FileTransferObject( file_info_dict[ 'directory' ], \
py-files/manage_stat_arb_symbols (2).py:        hsutils.debug( log_fh, str( sql ) )
py-files/manage_stat_arb_symbols (2).py:       hsutils.raise_error( 'No rows affected. Exiting ...\n', True )
py-files/manage_stat_arb_symbols (2).py:       hsutils.debug( log_fh, 'No. of rows affected: ' + str( rows_affected ) )
py-files/manage_stat_arb_symbols (2).py:    hsutils.debug(log_fh, "Finding outgoing symbols using:\n\n" + sql + "\n\n")
py-files/manage_stat_arb_symbols (2).py:       hsutils.debug(log_fh, "\n\nNone Found.\n\n")
py-files/manage_stat_arb_symbols (2).py:       hsutils.debug(log_fh, "Executing:\n" + delete_command)
py-files/manage_stat_arb_symbols (2).py:       results = hsutils.run_cmd(delete_command, 600)
py-files/manage_stat_arb_symbols (2).py:              mail = hsutils.HeliosEmail()
py-files/manage_stat_arb_symbols (2).py:    hsutils.debug(log_fh, "\n\nFinding incoming symbols using:\n" + sql + "\n\n")
py-files/manage_stat_arb_symbols (2).py:       hsutils.debug(log_fh, "\n\nNone Found.\n\n")
py-files/manage_stat_arb_symbols (2).py:       hsutils.debug(log_fh, "Executing:\n" + add_command)
py-files/manage_stat_arb_symbols (2).py:       results = hsutils.run_cmd(add_command, 600)
py-files/manage_stat_arb_symbols (2).py:              mail = hsutils.HeliosEmail()
py-files/manage_stat_arb_symbols (2).py:    hsutils.debug( log_fh, "Executing SQL to update target positions to ZERO:\n\n" + str( sql ) + "\n\n" )
py-files/manage_stat_arb_symbols (2).py:       hsutils.raise_error( 'No rows affected. Exiting ...\n', True )
py-files/manage_stat_arb_symbols (2).py:       hsutils.debug( log_fh, 'No. of rows affected: ' + str( rows_affected ) )
py-files/manage_strategy_symbols (2).py:import hsutils
py-files/manage_strategy_symbols (2).py:                 choices=hsutils.get_valid_business_unit_codes(),
py-files/manage_strategy_symbols (2).py:sys_conn_string = hsutils.getSystemConnectionString(args.business_unit_code)
py-files/mass_cancel (2).py:import hsutils
py-files/mass_cancel (2).py:        helios_db = hsutils.db_conn.getSystemConnectionString( business_unit_code )
py-files/mass_cancel (2).py:            results = hsutils.run_cmd( cmd )
py-files/mass_cancel (2).py:                     choices = hsutils.db_conn.get_valid_business_unit_codes(),
py-files/mass_cancel (2).py:    db_conn_data = hsutils.db_conn.getSystemConnectionDict(args.business_unit_code)
py-files/mass_cancel (2).py:    db = hsutils.db_conn.TransactionalDB(host = db_conn_data['host'],
py-files/mbm_autoadjust (2).py:import hsutils
py-files/mbm_autoadjust (2).py:                     choices = hsutils.db_conn.get_valid_business_unit_codes(),
[root@linuxserver pytontest]# find py-files/ -type f -print0 | xargs -r0 grep -F 'hsutils'
