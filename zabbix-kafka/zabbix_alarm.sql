/*
 Navicat Premium Data Transfer

 Source Server         : 192.20.32.26
 Source Server Type    : MySQL
 Source Server Version : 50560
 Source Host           : 192.20.32.26:3306
 Source Schema         : cmdb

 Target Server Type    : MySQL
 Target Server Version : 50560
 File Encoding         : 65001

 Date: 07/05/2020 09:56:33
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for zabbix_alarm
-- ----------------------------
DROP TABLE IF EXISTS `zabbix_alarm`;
CREATE TABLE `zabbix_alarm`  (
  `eventid` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL COMMENT '事件id',
  `groupname` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL COMMENT '主机组',
  `hostname` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL COMMENT '主机名称',
  `ip` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL COMMENT '主机ip',
  `description` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL COMMENT '主机描述',
  `trigger_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL COMMENT '触发器名字',
  `alarm_level` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL COMMENT '告警等级',
  `alarm_type` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL,
  `alarm_time` datetime NULL DEFAULT NULL COMMENT '告警时间',
  `recover_time` datetime NULL DEFAULT NULL COMMENT '恢复时间',
  `alarm_value` text CHARACTER SET utf8 COLLATE utf8_bin NULL COMMENT '告警值',
  `recover_value` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL COMMENT '恢复值',
  `tag` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL COMMENT '标签',
  `备注` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL COMMENT '故障说明',
  PRIMARY KEY (`eventid`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

SET FOREIGN_KEY_CHECKS = 1;
